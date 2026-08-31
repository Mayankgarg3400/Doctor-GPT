# 🩺 Doctor-GPT

### AI-Powered Medical Assistance Platform

Doctor-GPT is an AI-powered medical assistance platform that provides multiple ways to interact with an intelligent healthcare assistant through **Text, Vision, Voice, and Emergency Assistance**.


> ⚠️ **Medical Disclaimer:** Doctor-GPT is an AI-based assistance and educational project. It is not a replacement for a qualified doctor or medical professional. For serious symptoms, diagnosis, treatment decisions, or emergencies, always consult a qualified healthcare professional or contact your local emergency services.


## 🖥️ Project Preview

![Doctor-GPT](https://github.com/Mayankgarg3400/Doctor-GPT/blob/main/doctor-gpt.jpg)
---

## ✨ Features

### 💬 Text-Based Medical Assistant

Ask medical and health-related questions using natural language and receive AI-generated responses.

### 👁️ Vision-Based Medical Assistant

Upload an image and interact with the AI system for image-based medical analysis.

### 🎙️ Voice Interaction

Doctor-GPT includes a voice interaction pipeline supporting:

* 🎤 Speech-to-Text
* 🧠 AI-powered response generation
* 🔊 Text-to-Speech

### 🚨 Emergency Assistant

A dedicated emergency assistant provides emergency-focused guidance and helps users understand appropriate immediate actions.

### 🧠 Medical Knowledge Retrieval

The project includes a medical knowledge retrieval pipeline that retrieves relevant information from a medical knowledge base before generating responses.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │     Doctor-GPT      │
                         │     Web Interface   │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
      Text Assistant        Vision Assistant       Emergency Assistant
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Python Backend    │
                         │    FastAPI / API    │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
             Medical RAG                       AI Models
          Knowledge Retrieval              LLM / Vision Models
                    │
                    ▼
             Medical Knowledge
```

---

# 📂 Project Structure

```text
Doctor-GPT/
│
├── doctor-gpt-site/
│   ├── index.html
│   ├── choose.html
│   ├── text.html
│   ├── vision.html
│   ├── emergency.html
│   ├── chat.js
│   ├── text.js
│   ├── vision.js
│   └── style.css
│
├── Text_backend/
│   ├── __init__.py
│   └── memory_collection.py
│
├── emergency_backend/
│   ├── __init__.py
│   ├── ai_agent.py
│   └── tools.py
│
├── vision_backend/
│   ├── brain.py
│   ├── merge.py
│   ├── voice_of_doctor.py
│   └── voice_of_user.py
│
├── medical-chatbot/
│   ├── brain_of_the_doctor.py
│   ├── connect_memory_with_llm.py
│   ├── create_memory_for_llm.py
│   └── medibot.py
│
├── main.py
├── server.py
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

| Category           | Technologies                                       |
| ------------------ | -------------------------------------------------- |
| Frontend           | HTML5, CSS3, JavaScript                            |
| Backend            | Python, FastAPI, Uvicorn                           |
| AI / LLM           | Ollama, Qwen-based models                          |
| RAG                | LangChain, FAISS                                   |
| Voice              | SpeechRecognition, Google Speech Recognition, gTTS |
| Version Control    | Git, GitHub                                        |
| Package Management | uv                                                 |
| Development        | VS Code                                            |

---

# ⚙️ How It Works

## 1. 💬 Text Assistant

```text
User Question
      ↓
Web Interface
      ↓
Backend API
      ↓
Medical Knowledge Retrieval
      ↓
LLM
      ↓
Generated Response
      ↓
User
```

## 2. 👁️ Vision Assistant

```text
Medical Image
      ↓
Web Interface
      ↓
Vision Backend
      ↓
Vision AI Model
      ↓
Image Analysis
      ↓
Response
```

## 3. 🎙️ Voice Assistant

```text
User Speech
      ↓
Speech-to-Text
      ↓
AI Assistant
      ↓
Generated Response
      ↓
Text-to-Speech
      ↓
Audio Response
```

## 4. 🚨 Emergency Assistant

```text
Emergency Query
      ↓
Emergency Backend
      ↓
AI Agent + Tools
      ↓
Emergency Guidance
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root and add the required API keys.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

> 🔒 Never upload API keys, passwords, tokens, or other secrets to GitHub.

The `.gitignore` file is configured to prevent `.env` files from being committed.

---

# 💻 Local Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Mayankgarg3400/Doctor-GPT.git
cd Doctor-GPT
```

## 2. Install Dependencies

Doctor-GPT uses `uv` for Python dependency management.

```bash
uv sync
```

## 3. Configure Environment Variables

Create a `.env` file and add the required configuration.

## 4. Start the Backend

```bash
uv run uvicorn server:app --reload
```

Depending on the configured application entry point, the backend may also be started with:

```bash
uv run uvicorn main:app --reload
```

## 5. Open the Frontend

Open:

```text
doctor-gpt-site/index.html
```

or serve the frontend using a local development server.

---

# 🔌 Application Flow

```text
                     USER
                       │
                       ▼
              ┌─────────────────┐
              │   Web Interface │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
        TEXT         VISION       VOICE
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Python Backend  │
              └────────┬────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Medical RAG           AI Models
             │                   │
             └─────────┬─────────┘
                       ▼
                  AI Response
                       │
                       ▼
                     USER
```

---

# 🔒 Security

Doctor-GPT follows basic security practices:

* API keys are stored using environment variables.
* `.env` files are excluded from Git.
* Large medical datasets are excluded from the repository.
* Generated vector stores are excluded from Git.
* Private credentials should never be placed inside frontend JavaScript.

---

# 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

# ⚠️ Medical Disclaimer

Doctor-GPT generates AI-based information and should not be considered professional medical advice.

The system may produce incorrect or incomplete information.

For serious symptoms, diagnosis, treatment decisions, or emergencies, consult a qualified healthcare professional or contact your local emergency services.

---

# 👨‍💻 Author

### Mayank Garg

🔗 **GitHub:** [Mayankgarg3400](https://github.com/Mayankgarg3400)

---

⭐ If you find this project useful, consider giving the repository a star!
