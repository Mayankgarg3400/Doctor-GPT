from gtts import gTTS


def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    output_file = "doctor_response.mp3"
    tts.save(output_file)

    return output_file