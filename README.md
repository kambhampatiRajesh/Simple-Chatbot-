# 🤖 ChatGPT-Style AI Chatbot

**Powered by Streamlit · n8n · Google Gemini LLM**

A production-ready conversational AI chatbot that behaves like ChatGPT, built using a **Streamlit web application** for the UI and **n8n automation workflows** for backend orchestration — powered by **Google Gemini LLM** with context memory.

This project was built during my **Gen AI Internship at Innomatics Research Labs** and demonstrates how modern LLMs can be integrated into scalable, real-time AI systems using low-code tools.

---

##  Features

*  **ChatGPT-like conversational experience**
*  **Context-aware responses** using memory integration
*  **Streamlit Web UI** for clean, interactive chat
*  **n8n workflow backend** for message routing and LLM handling
*  **Google Gemini LLM** for intelligent, human-like responses
*  Real-time request/response via webhooks
*  Modular design — easy to extend with new actions

---

##  How It Works

1. User sends a message through the **Streamlit chat UI**
2. Streamlit sends the message to an **n8n Webhook**
3. n8n processes the input using:

   * AI Agent (Google Gemini)
   * Memory node (conversation context)
4. Gemini generates a contextual response
5. n8n sends the response back to Streamlit
6. Streamlit renders the reply instantly

---

##  System Architecture

```
User → Streamlit Web App
        ↓
     n8n Webhook
        ↓
   Gemini LLM + Memory
        ↓
   Response to Webhook
        ↓
 Streamlit Chat UI
```

---

##  Tech Stack

* **Streamlit** – Frontend chat interface
* **n8n** – Workflow automation & orchestration
* **Google Gemini LLM** – Conversational intelligence
* **Python** – Application logic
* **Webhooks** – Real-time communication
* **Context Memory** – Multi-turn conversation handling

---

##  Why This Project Matters

This project goes beyond a basic chatbot. It demonstrates:

* Real-world **LLM application design**
* Clean **frontend ↔ backend separation**
* **No-code + low-code automation** with n8n
* Scalable architecture for AI assistants
* Cost-efficient alternative to heavy backend systems

---

##  Use Cases

* Customer Support Chatbot
* AI Mentor / Tutor
* Internal Knowledge Assistant
* Email & Workflow Automation Bot
* Personal AI Assistant

---

## 🛠️ Setup Instructions

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
N8N_WEBHOOK_URL=your_n8n_webhook_url
```

###  Run Streamlit App

```bash
streamlit run app.py
```

###  Start n8n Workflow

* Import the provided n8n workflow JSON
* Activate the workflow
* Ensure webhook is publicly accessible

---

##  Future Enhancements

* Tool calling (search, APIs, databases)
* Authentication & user sessions
* Persistent memory storage
* Deployment on cloud platforms
* Multi-agent support
---

##  Support

If you found this project useful, feel free to ⭐ the repository!

---


Just tell me 👍
