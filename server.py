from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os

from vision_backend.brain import encode_image, get_response
from emergency_backend.ai_agent import agentic
from Text_backend.memory_collection import doctor_gpt_backend


app = FastAPI(title="Doctor-GPT")


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Doctor-GPT API is running"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ============================================================
# TEXT BOT
# ============================================================

@app.post("/Text_Bot")
def text_bot(query: str = Form(...)):

    response = doctor_gpt_backend(query)

    return {
        "response": response
    }


# ============================================================
# EMERGENCY BOT
# ============================================================

@app.post("/Emergency_Bot")
def emergency_bot(query: str = Form(...)):

    response = agentic(query)

    return {
        "response": response
    }


# ============================================================
# VISION BOT
# ============================================================

@app.post("/ask")
async def ask_doctor(
    image: UploadFile = File(...),
    question: str = Form(...)
):

    suffix = os.path.splitext(image.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(await image.read())
        image_path = temp.name

    try:
        encoded_image = encode_image(image_path)

        response = get_response(
            encoded_image,
            question
        )

        return {
            "response": response["Message"]
        }

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)


# ============================================================
# VISION BOT - IMAGE ONLY
# ============================================================

@app.post("/Vision_Bot/Image")
async def vision_bot_image(
    image: UploadFile = File(...)
):

    suffix = os.path.splitext(image.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp:

        temp.write(await image.read())
        image_path = temp.name

    try:
        encoded_image = encode_image(image_path)

        response = get_response(
            encoded_image,
            "Describe what you see in this image."
        )

        return {
            "answer": response["Message"]
        }

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)