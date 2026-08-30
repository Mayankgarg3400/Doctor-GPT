# # from fastapi import FastAPI, UploadFile, File, Form
# # import tempfile
# # import os

# # from vision_backend.brain import encode_image, get_response


# # app = FastAPI(title="Doctor-GPT")


# # @app.get("/")
# # def root():
# #     return {
# #         "message": "Doctor-GPT API is running"
# #     }


# # @app.get("/health")
# # def health():
# #     return {
# #         "status": "healthy"
# #     }


# # @app.post("/ask")
# # async def ask_doctor(
# #     image: UploadFile = File(...),
# #     question: str = Form(...)
# # ):
# #     suffix = os.path.splitext(image.filename)[1]

# #     with tempfile.NamedTemporaryFile(
# #         delete=False,
# #         suffix=suffix
# #     ) as temp:
# #         temp.write(await image.read())
# #         image_path = temp.name

# #     try:
# #         encoded_image = encode_image(image_path)

# #         response = get_response(
# #             encoded_image,
# #             question
# #         )

# #         return {
# #             "response": response["Message"]
# #         }

# #     finally:
# #         os.remove(image_path)

# from fastapi import FastAPI, UploadFile, File, Form
# import tempfile
# import os

# from vision_backend.brain import encode_image, get_response
# from emergency_backend.ai_agent import agentic

# app = FastAPI(title="Doctor-GPT")


# # ============================================================
# # ROOT
# # ============================================================

# @app.get("/")
# def root():
#     return {
#         "message": "Doctor-GPT API is running"
#     }


# # ============================================================
# # HEALTH
# # ============================================================

# @app.get("/health")
# def health():
#     return {
#         "status": "healthy"
#     }


# # ============================================================
# # VISION BOT
# # ============================================================

# @app.post("/ask")
# async def ask_doctor(
#     image: UploadFile = File(...),
#     question: str = Form(...)
# ):

#     suffix = os.path.splitext(image.filename)[1]

#     with tempfile.NamedTemporaryFile(
#         delete=False,
#         suffix=suffix
#     ) as temp:

#         temp.write(await image.read())
#         image_path = temp.name

#     try:

#         encoded_image = encode_image(image_path)

#         response = get_response(
#             encoded_image,
#             question
#         )

#         return {
#             "response": response["Message"]
#         }

#     finally:

#         if os.path.exists(image_path):
#             os.remove(image_path)


# # ============================================================
# # EMERGENCY BOT
# # ============================================================

# @app.post("/Emergency_Bot")
# async def emergency_bot(query: str = Form(...)):

#     response = agentic(query)

#     return {
#         "response": response
#     }

# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import tempfile
# import os

# from fastapi.middleware.cors import CORSMiddleware

# from vision_backend.brain import encode_image, get_response
# from emergency_backend.ai_agent import agentic
# from Text_backend.memory_collection import doctor_gpt_backend


# app = FastAPI(title="Doctor-GPT")
from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import tempfile
import os

from fastapi.middleware.cors import CORSMiddleware

from vision_backend.brain import encode_image, get_response
from emergency_backend.ai_agent import agentic
from Text_backend.memory_collection import doctor_gpt_backend


app = FastAPI(title="Doctor-GPT")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST MODELS
# ============================================================

class TextBotRequest(BaseModel):
    query: str


class EmergencyRequest(BaseModel):
    query: str


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Doctor-GPT API is running"
    }


# ============================================================
# HEALTH
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
def text_bot(data: TextBotRequest):

    response = doctor_gpt_backend(data.query)

    return {
        "response": response
    }


# ============================================================
# EMERGENCY BOT
# ============================================================

@app.post("/Emergency_Bot")
def emergency_bot(data: EmergencyRequest):

    response = agentic(data.query)

    return {
        "response": response
    }


# ============================================================
# VISION BOT - OLD ENDPOINT
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
# VISION BOT - GITHUB FRONTEND ENDPOINT
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