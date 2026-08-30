const imageInput = document.getElementById("imageInput");
const previewImg = document.getElementById("preview-img");

const questionInput = document.getElementById("questionInput");

const recordBtn = document.getElementById("recordBtn");
const analyzeBtn = document.getElementById("analyzeBtn");

const statusText = document.getElementById("status");

const resultBox = document.getElementById("resultBox");
const answerBox = document.getElementById("answer");

const speakAnswerBtn =
    document.getElementById("speakAnswerBtn");


// ============================================================
// IMAGE PREVIEW
// ============================================================

imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if (!file) {
        return;
    }

    previewImg.src = URL.createObjectURL(file);

    previewImg.style.display = "block";

    resultBox.style.display = "none";

    statusText.textContent =
        "Image selected successfully.";

});


// ============================================================
// VOICE INPUT
// ============================================================

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;


let recognition = null;


if (SpeechRecognition) {

    recognition = new SpeechRecognition();

    recognition.lang = "en-US";

    recognition.interimResults = false;

    recognition.continuous = false;


    recognition.onstart = () => {

        recordBtn.textContent =
            "🔴 Listening...";

        recordBtn.classList.add("recording");

        statusText.textContent =
            "Listening... Please speak your question.";

    };


    recognition.onresult = (event) => {

        const transcript =
            event.results[0][0].transcript;

        questionInput.value = transcript;

        statusText.textContent =
            "Voice question captured.";

    };


    recognition.onerror = (event) => {

        console.error(
            "Speech recognition error:",
            event.error
        );

        statusText.textContent =
            "❌ Could not understand your voice.";

    };


    recognition.onend = () => {

        recordBtn.textContent =
            "🎤 Speak";

        recordBtn.classList.remove("recording");

    };

} else {

    recordBtn.disabled = true;

    recordBtn.textContent =
        "🎤 Voice not supported";

}


// ============================================================
// SPEAK BUTTON
// ============================================================

recordBtn.addEventListener("click", () => {

    if (!recognition) {

        alert(
            "Voice recognition is not supported by this browser."
        );

        return;

    }

    recognition.start();

});


// ============================================================
// ANALYZE IMAGE
// ============================================================

analyzeBtn.addEventListener(
    "click",
    async () => {

        const imageFile =
            imageInput.files[0];

        const question =
            questionInput.value.trim();


        // Check image

        if (!imageFile) {

            alert(
                "Please upload an image first."
            );

            return;

        }


        // Check question

        if (!question) {

            alert(
                "Please ask a question about the image."
            );

            questionInput.focus();

            return;

        }


        // Disable button

        analyzeBtn.disabled = true;

        analyzeBtn.textContent =
            "🧠 Analyzing...";


        statusText.textContent =
            "DoctorGPT is analyzing the image...";


        resultBox.style.display = "none";


        // FormData

        const formData = new FormData();

        formData.append(
            "image",
            imageFile
        );

        formData.append(
            "question",
            question
        );


        try {

            const response =
                await fetch(
                    "http://127.0.0.1:8000/ask",
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


            const data =
                await response.json();


            // Show answer

            answerBox.textContent =
                data.response;


            resultBox.style.display =
                "block";


            statusText.textContent =
                "✅ Analysis completed.";


            // Scroll to result

            resultBox.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });


        } catch (error) {

            console.error(
                "Vision Bot Error:",
                error
            );


            statusText.textContent =
                "❌ Unable to connect to DoctorGPT server.";

        }


        analyzeBtn.disabled = false;

        analyzeBtn.textContent =
            "🔍 Analyze Image";

    }
);


// ============================================================
// TEXT TO SPEECH
// ============================================================

speakAnswerBtn.addEventListener(
    "click",
    () => {

        const text =
            answerBox.textContent.trim();


        if (!text) {

            return;

        }


        // Stop previous speech

        window.speechSynthesis.cancel();


        const speech =
            new SpeechSynthesisUtterance(text);


        speech.lang = "en-US";

        speech.rate = 0.95;

        speech.pitch = 1;


        speakAnswerBtn.textContent =
            "🔊 Speaking...";


        speech.onend = () => {

            speakAnswerBtn.textContent =
                "🔊 Speak Answer";

        };


        window.speechSynthesis.speak(
            speech
        );

    }
);