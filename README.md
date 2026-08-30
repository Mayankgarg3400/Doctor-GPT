# 🩺 Doctor-GPT

**Doctor-GPT** is an AI-powered medical assistance platform designed to provide users with multiple ways to interact with an intelligent healthcare assistant through **text, vision, voice, and emergency assistance**.

> ⚠️ **Medical Disclaimer:** Doctor-GPT is an AI-based assistance and educational project. It is not a replacement for a qualified doctor or medical professional. For serious symptoms, diagnosis, treatment decisions, or emergencies, always consult a qualified healthcare professional or contact your local emergency services.

---

## ✨ Features

### 💬 Text-Based Medical Assistant

Users can ask medical and health-related questions using natural language and receive AI-generated responses.

### 👁️ Vision-Based Medical Assistant

Users can upload an image and interact with the AI system for image-based medical analysis.

### 🎙️ Voice Interaction

Doctor-GPT includes a voice interaction pipeline that supports:

* 🎤 Speech-to-text
* 🧠 AI-based response generation
* 🔊 Text-to-speech

### 🚨 Emergency Assistant

A dedicated emergency assistant provides emergency-focused guidance and helps users understand appropriate immediate actions.

### 🧠 Medical Knowledge Retrieval

The project includes a medical knowledge retrieval pipeline using a vector database to retrieve relevant information before generating responses.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │    Doctor-GPT UI    │
                         │     HTML/CSS/JS     │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
        Text Assistant       Vision Assistant     Emergency Assistant
              │                     │                     │
              └─────────────────────┼─────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Python Backend    │
                         │   FastAPI / APIs    │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         ▼                     ▼
                  Medical RAG             AI Models
                  / Vector Store          / LLM / Vision
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

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* FastAPI
* Uvicorn

## AI / LLM

* Ollama
* Qwen-based local models
* AI-powered response generation

## RAG / Knowledge Retrieval

* LangChain
* FAISS
* Medical knowledge base

## Voice

* SpeechRecognition
* Google Speech Recognition
* gTTS

## Development Tools

* Git
* GitHub
* uv
* VS Code

---

# ⚙️ How It Works

## 1️⃣ Text Assistant

```text
User Question
      ↓
Frontend
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

---

## 2️⃣ Vision Assistant

```text
Medical Image
      ↓
Frontend
      ↓
Vision Backend
      ↓
Vision-capable AI Model
      ↓
Image Analysis
      ↓
Response
```

---

## 3️⃣ Voice Assistant

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

---

## 4️⃣ Emergency Assistant

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

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

> Never commit API keys or other secrets to GitHub.

The `.gitignore` file is configured to prevent `.env` files from being uploaded.

---

# 💻 Local Setup

## 1. Clone the repository

```bash
git clone https://github.com/Mayankgarg3400/Doctor-GPT.git
cd Doctor-GPT
```

## 2. Install dependencies

This project uses `uv` for Python dependency management.

```bash
uv sync
```

## 3. Configure environment variables

Create a `.env` file:

```text
.env
```

Add the required API keys and configuration.

## 4. Start the backend

Depending on the configured backend entry point:

```bash
uv run uvicorn server:app --reload
```

or:

```bash
uv run uvicorn main:app --reload
```

## 5. Start the frontend

Open the frontend:

```text
doctor-gpt-site/index.html
```

You can also serve the frontend using a local web server.

---

# 🔌 API Communication

The frontend communicates with the Python backend through API endpoints.

General flow:

```text
Frontend
   ↓
API Request
   ↓
Python Backend
   ↓
AI / RAG / Vision / Emergency Module
   ↓
AI Response
   ↓
Frontend
```

---

# 🔒 Security

The project follows basic security practices:

* API keys are stored using environment variables.
* `.env` files are excluded from Git.
* Large medical datasets are excluded from the public repository.
* Generated vector stores are excluded from Git.
* Private credentials should never be exposed in frontend JavaScript.

---

# 📌 Current Project Status

### Implemented

* ✅ Text-based medical assistant
* ✅ Vision-based assistant
* ✅ Voice interaction pipeline
* ✅ Emergency assistant
* ✅ Medical knowledge retrieval
* ✅ Frontend interfaces
* ✅ Python backend
* ✅ GitHub repository

### In Progress / Planned

* 🚀 Production deployment
* 🔐 Improved authentication and security
* 📊 Logging and monitoring
* 🧠 Improved medical RAG pipeline
* ⚡ Performance optimization
* 📱 Improved mobile UI
* 🌐 Production-ready hosting

---

# 🗺️ Future Improvements

Some planned improvements include:

* Multi-model support
* Better medical document retrieval
* Conversation history
* User authentication
* Database integration
* Improved emergency workflows
* Production monitoring
* Cloud deployment
* Better mobile responsiveness

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

**Mayank Garg**

GitHub:
https://github.com/Mayankgarg3400

---

⭐ If you find this project useful, consider giving the repository a star!
