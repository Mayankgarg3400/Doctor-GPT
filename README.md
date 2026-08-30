
# 🩺 Doctor-GPT

An AI-powered medical assistance platform that provides multiple ways to interact with an intelligent healthcare assistant — through **text, vision, voice, and emergency assistance**.

> ⚠️ **Medical Disclaimer:** Doctor-GPT is an AI-based educational and assistance tool. It is not a replacement for a qualified doctor or emergency medical professional. Always seek professional medical advice for diagnosis, treatment, or urgent medical situations.

---

## 🚀 Features

### 💬 Text-Based Medical Assistant
Ask medical and health-related questions using natural language and receive AI-generated responses.

### 👁️ Vision-Based Medical Assistant
Upload an image and interact with the AI assistant for image-based medical analysis.

### 🎙️ Voice Interaction
Doctor-GPT supports voice-based interaction:
- Speech-to-text for user input
- AI-generated response
- Text-to-speech for spoken responses

### 🚨 Emergency Assistant
Provides an emergency-focused interface designed to help users identify appropriate immediate actions and guidance.

### 🧠 Medical Knowledge / RAG
The project includes a medical knowledge pipeline using a vector database to retrieve relevant information before generating responses.

---

## 🏗️ Project Architecture

```text
                         ┌─────────────────────┐
                         │    Doctor-GPT UI    │
                         │  HTML / CSS / JS    │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
              Text Assistant   Vision Assistant  Emergency
                    │               │               │
                    └───────────────┼───────────────┘
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
                  Vector Store           / LLM / Vision
                         │
                         ▼
                  Medical Knowledge



📂 Project Structure
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


🛠️ Tech Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Python
FastAPI
Uvicorn
AI / LLM
Ollama
Qwen-based local models
AI-powered medical response generation
RAG / Knowledge Retrieval
LangChain
FAISS
Medical knowledge base
Voice
SpeechRecognition
Google Speech Recognition
gTTS (Google Text-to-Speech)
Development Tools
Git
GitHub
uv
VS Code
⚙️ How Doctor-GPT Works
1. Text Assistant
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
2. Vision Assistant
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
3. Voice Assistant
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
4. Emergency Assistant
Emergency Query
      ↓
Emergency Backend
      ↓
AI Agent + Tools
      ↓
Emergency Guidance

⚠️ Disclaimer

Doctor-GPT provides AI-generated information and should not be considered professional medical advice.

For serious symptoms, emergencies, diagnosis, or treatment decisions, consult a qualified healthcare professional or contact your local emergency services.

👨‍💻 Author

Mayank Garg

GitHub:
https://github.com/Mayankgarg3400

⭐ If you find this project useful, consider giving the repository a star!
