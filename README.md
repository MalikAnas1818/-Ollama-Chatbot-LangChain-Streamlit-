# 🤖 Ollama Chatbot (LangChain + Streamlit)

This is a simple AI chatbot project built using:

- 🧠 LangChain + LLMChain
- 🐍 Ollama running LLaMA 3 locally
- 🌐 Streamlit for a web-based chat interface

It is trained (prompted) to identify itself as an AI assistant built by **Muhammad Anis**, and it responds accordingly if the user asks for its name or creator.

---

## 📦 Features

- 💬 Ask any question using a text box
- 🧠 Responses powered by `llama3` running through Ollama
- 🕘 Conversation history panel in the sidebar
- 🔁 Reset button to clear conversation
- ✅ Lightweight and easy to run on local machine

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/ollama-chatbot
cd ollama-chatbot

## 2. Create a Virtual Environment
   python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt
  
# 🧠 Make Sure Ollama is Installed
#### This app requires Ollama installed and running on your system.

Download: https://ollama.com

Install a model like LLaMA 3.2:
ollama pull llama3.2
Make sure ollama works in your terminal:
ollama run llama3.2

## 🖥️ Running the App
streamlit run app.py
Visit the link shown in the terminal (usually http://localhost:8501)

## 🔧 Project Structure
📁 ollama-chatbot/
├── app.py               # Main Streamlit app

├── requirements.txt     # Python dependencies

└── README.md            # Project overview and instructions

## 🧠 Example Prompt Logic
### If user asks: "What is your name?", the bot will respond:

### "I was trained for Ollama by Muhammad Anis."

#### Otherwise, it answers the user's question helpfully.

# 🙋‍♂️ Author
## Muhammad Anis
### AI Agent Designer & Prompt Engineer

