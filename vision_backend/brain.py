import base64
import ollama


def encode_image(imagepath):
    with open(imagepath, "rb") as f:
        image_bytes = f.read()

    return base64.b64encode(image_bytes).decode("utf-8")


model = "qwen2.5vl:3b"


def get_response(encoded_image, query):

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                # "content": (
                #     "You are a medical assistant. "
                #     "Analyze the image carefully and answer clearly. "
                #     "Give the proper answer in 3-4 lines and only in paragraph form."
                # ),
                "content":(
                    
                "You are a medical AI assistant. "
                "Analyze the provided medical image carefully, but do not "
                "claim a definitive diagnosis from the image alone. "
                "Describe visible findings and mention possible conditions "
                "as possibilities only. "
                "Do not prescribe medicines or dosages. "
                "If the image suggests a potentially serious condition, "
                "recommend consulting a qualified healthcare professional. "
                "Keep the answer concise, around 3-5 lines, in paragraph form."
                                               ),
                "images": [base64.b64decode(encoded_image)],
            },
            {
                "role": "user",
                "content": query,
            },
        ],
    )

    return {"Message": response["message"]["content"]}