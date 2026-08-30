import speech_recognition as sr


def convert_speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""

    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return ""