from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

from emergency_backend.tools import (
    query_medgemma,
    call_emergency,
    Doctors_search,
)

load_dotenv()


# ============================================================
# TOOL 1: General Medical / Mental Health
# ============================================================

@tool
def ask_mental_health_specialist(query: str):
    """
    Generate a medical or mental-health response.

    Use this for general medical questions, emotional concerns,
    mental health questions and health-related guidance.
    """
    return query_medgemma(query)


# ============================================================
# TOOL 2: Emergency Call
# ============================================================

@tool
def emergency_call_tooling():
    """
    Place an emergency call.

    Use ONLY when the user explicitly asks for emergency help
    or immediate assistance.
    """
    return call_emergency()


# ============================================================
# TOOL 3: Nearby Doctors / Hospitals
# ============================================================

@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Find nearby hospitals or doctors using the given location.
    """
    return Doctors_search(location)


# ============================================================
# ROUTER PROMPT
# ============================================================

ans = PromptTemplate(
    template="""
You are an emergency medical assistant.

Your job is to decide which tool should handle the user's request.

TOOLS:

1. ask_mental_health_specialist
Use for:
- General medical questions
- Symptoms
- Health information
- Mental health questions
- Emotional concerns

Examples:
"What are symptoms of dengue?"
"What should I do for a headache?"
"I feel very anxious."

2. find_nearby_therapists_by_location
Use for:
- Finding hospitals
- Finding doctors
- Finding medical facilities near a location

Examples:
"Find hospitals near Delhi"
"Show doctors near Noida"
"Hospital near Chandigarh"

3. emergency_call_tooling
Use ONLY when the user explicitly requests immediate emergency help.

Examples:
"Call emergency services"
"I need emergency help"
"Call ambulance now"

IMPORTANT:
- Do not call emergency_call_tooling for ordinary medical questions.
- Do not call it merely because symptoms sound serious.
- If the user asks for a hospital/doctor near a location, use the location tool.
- For general health questions, use the medical tool.

USER QUERY:
{input}
""",
    input_variables=["input"],
)


# ============================================================
# LOCAL OLLAMA ROUTER
# ============================================================

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
)


Tools = [
    ask_mental_health_specialist,
    emergency_call_tooling,
    find_nearby_therapists_by_location,
]

model_binded = model.bind_tools(Tools)


# ============================================================
# AGENT
# ============================================================

def agentic(query: str):

    prompt = ans.invoke({
        "input": query
    })

    messages = [
        HumanMessage(content=prompt.text)
    ]

    response = model_binded.invoke(messages)

    # --------------------------------------------------------
    # TOOL CALL
    # --------------------------------------------------------

    if response.tool_calls:

        final_results = []

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            tools_map = {
                "ask_mental_health_specialist":
                    ask_mental_health_specialist,

                "find_nearby_therapists_by_location":
                    find_nearby_therapists_by_location,

                "emergency_call_tooling":
                    emergency_call_tooling,
            }

            selected_tool = tools_map.get(tool_name)

            if selected_tool is None:
                continue

            tool_output = selected_tool.invoke(tool_args)

            final_results.append(
                str(tool_output)
            )

        # ----------------------------------------------------
        # FINAL RESPONSE
        # ----------------------------------------------------

        final_prompt = f"""
You are Doctor AI, a compassionate emergency medical assistant.

USER:
{query}

TOOL RESULT:
{chr(10).join(final_results)}

Give the user a clear and supportive response.

Rules:

- Do not mention tools or APIs.
- Do not show internal processing.
- Do not show JSON.
- Keep the response concise.
- For emergency situations, encourage the user to seek
  immediate professional emergency help.
- For hospital searches, present results as a clean list.
- For general medical questions, explain simply.
"""

        formatter = ChatOllama(
            model="qwen2.5:3b",
            temperature=0.3,
        )

        final_answer = formatter.invoke(final_prompt)

        return final_answer.content

    # --------------------------------------------------------
    # NO TOOL
    # --------------------------------------------------------

    return (
        "I am Doctor AI and can help with medical questions, "
        "nearby hospitals/doctors, and emergency assistance."
    )