const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");


function addMessage(text, sender) {

    const div = document.createElement("div");

    div.classList.add("message", sender);

    div.textContent = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

    return div;
}


async function sendMessage() {

    const msg = userInput.value.trim();

    if (!msg) {
        return;
    }


    // Show user message
    addMessage(msg, "user");

    userInput.value = "";


    // Disable button while AI responds
    sendBtn.disabled = true;
    userInput.disabled = true;


    // Typing indicator
    const typingMessage = addMessage(
        "DoctorGPT is typing...",
        "typing"
    );


    try {

        /*
         * IMPORTANT:
         * FastAPI expects:
         *
         * query: str = Form(...)
         *
         * Therefore we must send FormData.
         */

        const formData = new FormData();

        formData.append("query", msg);


        const response = await fetch(
            "http://127.0.0.1:8000/Text_Bot",
            {
                method: "POST",
                body: formData
            }
        );


        if (!response.ok) {

            throw new Error(
                `Server error: ${response.status}`
            );

        }


        const data = await response.json();


        // Remove typing message
        typingMessage.remove();


        // Display AI response
        addMessage(
            data.response,
            "ai"
        );


    } catch (error) {

        console.error("Text Bot Error:", error);


        typingMessage.remove();


        addMessage(
            "❌ Unable to connect to DoctorGPT server. Please try again.",
            "ai"
        );

    }


    // Enable input again
    sendBtn.disabled = false;
    userInput.disabled = false;

    userInput.focus();
}


userInput.addEventListener(
    "keypress",
    function (event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);