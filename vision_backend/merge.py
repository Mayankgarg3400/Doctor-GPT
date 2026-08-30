from vision_backend.brain import encode_image, get_response
from vision_backend.voice_of_user import convert_speech_to_text
from vision_backend.voice_of_doctor import text_to_speech

def main(image_path):

    print("🎤 Listening...")
    query = convert_speech_to_text()

    if not query:
        print("Could not understand your voice.")
        return

    print("🧠 Doctor AI is thinking...")

    encoded_image = encode_image(image_path)

    response = get_response(
        encoded_image,
        query
    )

    doctor_response = response["Message"]

    print("\nDoctor AI:")
    print(doctor_response)

    audio_file = text_to_speech(doctor_response)

    print(f"\n🔊 Audio saved: {audio_file}")


if __name__ == "__main__":

    image_path = input("Enter image path: ")

    main(image_path)