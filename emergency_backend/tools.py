# ============================================================
# Emergency Backend Tools
# ============================================================

import os

import httpx
import ollama

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


# ============================================================
# TOOL 1
# Medical / Mental Health Assistant
# ============================================================

def query_medgemma(prompt: str) -> str:
    """
    Calls the local Ollama medical assistant.

    GitHub architecture keeps this as query_medgemma().
    We use qwen2.5:3b because it is already installed
    and working in this project.
    """

    system_prompt = """
You are Dr. Emily Hartman, a warm and experienced
medical and mental-health assistant.

Your responsibilities:

1. Only answer medical or health-related questions.
2. Explain medical information clearly and simply.
3. Be empathetic and supportive.
4. Never claim to diagnose a disease with certainty.
5. Never prescribe medicines or dosages.
6. If symptoms may be serious, recommend professional medical care.
7. If there is an emergency, recommend immediate emergency help.

If the user's query is NOT medical, respond exactly:

"I only answer medical questions. Please ask a health-related question."

Keep responses concise and easy to understand.
"""

    try:
        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            options={
                "num_predict": 400,
                "temperature": 0.7,
            },
        )

        return response["message"]["content"].strip()

    except Exception:
        return (
            "I'm having technical difficulties right now. "
            "Please try again shortly."
        )


# ============================================================
# TOOL 2
# Emergency Call using Twilio
# ============================================================

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
EMERGENCY_CONTACT = os.getenv("EMERGENCY_CONTACT")


def call_emergency():
    """
    Place an emergency call using Twilio.

    Do NOT call this function until Twilio credentials
    are configured in .env.
    """

    if not all(
        [
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN,
            TWILIO_FROM_NUMBER,
            EMERGENCY_CONTACT,
        ]
    ):
        return "Emergency calling is not configured."

    try:
        client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN,
        )

        client.calls.create(
            to=EMERGENCY_CONTACT,
            from_=TWILIO_FROM_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml",
        )

        return "Emergency Tool Called"

    except Exception:
        return (
            "Emergency calling is currently unavailable. "
            "Please contact emergency services directly."
        )


# ============================================================
# TOOL 3
# Nearby Doctors / Hospitals
# ============================================================

def Doctors_search(location: str) -> str:
    """
    Find nearby hospitals using:

    Nominatim
        ↓
    latitude / longitude
        ↓
    Overpass API
        ↓
    nearby hospitals
    """

    OSM = "https://nominatim.openstreetmap.org/search"

    # --------------------------------------------------------
    # Convert location -> latitude / longitude
    # --------------------------------------------------------

    def get_lat_lon(location: str):

        params = {
            "q": location,
            "format": "json",
            "limit": 1,
        }

        headers = {
            "User-Agent": "Doctor-GPT/1.0"
        }

        try:
            with httpx.Client(timeout=20) as client:
                response = client.get(
                    OSM,
                    params=params,
                    headers=headers,
                )

                response.raise_for_status()

                data = response.json()

            if not data:
                return None, None

            return (
                float(data[0]["lat"]),
                float(data[0]["lon"]),
            )

        except Exception as e:
            print("NOMINATIM ERROR:", repr(e))
            return None, None

    # --------------------------------------------------------
    # Find nearby hospitals
    # --------------------------------------------------------

    def get_nearby_hospitals(
        lat: float,
        lon: float,
        radius: int = 5000,
    ):

        url = "https://overpass-api.de/api/interpreter"

        query = f"""
        [out:json];
        node["amenity"="hospital"](around:{radius},{lat},{lon});
        out;
        """

        headers = {
            "User-Agent": "Doctor-GPT/1.0",
            "Accept": "application/json",
        }

        try:
            with httpx.Client(
                timeout=60,
                headers=headers,
            ) as client:

                response = client.post(
                    url,
                    data={"data": query},
                )

                response.raise_for_status()

                data = response.json()

            hospitals = []

            for item in data.get("elements", []):

                tags = item.get("tags", {})

                name = tags.get("name")

                if name:
                    hospitals.append(name)

            if not hospitals:
                return "No hospitals found nearby."

            return "\n".join(hospitals[:10])

        except Exception as e:

            print("OVERPASS ERROR:", repr(e))

            return (
                "Unable to search nearby hospitals right now."
            )

    # --------------------------------------------------------
    # Main search
    # --------------------------------------------------------

    lat, lon = get_lat_lon(location)

    if lat is None or lon is None:
        return "Could not find the specified location."

    return get_nearby_hospitals(lat, lon)