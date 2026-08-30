const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

function addMessage(text, sender) {
    const div = document.createElement("div");

    div.classList.add("message");
    div.classList.add(sender);

    div.textContent = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}


async function sendMessage() {

    const msg = userInput.value.trim();

    if (!msg) return;


    // Show user message
    addMessage(msg, "user");

    userInput.value = "";


    // Typing indicator
    const typingMessage =
        document.createElement("div");

    typingMessage.classList.add(
        "message",
        "ai"
    );

    typingMessage.textContent =
        "DoctorGPT is thinking...";

    chatBox.appendChild(
        typingMessage
    );

    chatBox.scrollTop =
        chatBox.scrollHeight;


    try {

        // Create FormData
        const formData =
            new FormData();

        formData.append(
            "query",
            msg
        );


        // Send to FastAPI
        const response =
            await fetch(
                "http://127.0.0.1:8000/Emergency_Bot",
                {
                    method: "POST",
                    body: formData
                }
            );


        if (!response.ok) {

            throw new Error(
                `HTTP error: ${response.status}`
            );

        }


        const data =
            await response.json();


        // Remove typing message
        typingMessage.remove();


        // Show AI response
        addMessage(
            data.response,
            "ai"
        );


    } catch (error) {

        console.error(
            "Emergency Bot Error:",
            error
        );


        typingMessage.remove();


        addMessage(
            "❌ Unable to connect to DoctorGPT server.",
            "ai"
        );

    }

}


userInput.addEventListener(
    "keypress",
    (event) => {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);