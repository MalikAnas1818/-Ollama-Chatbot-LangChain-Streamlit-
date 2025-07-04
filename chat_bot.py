import streamlit as st
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

# Initialize the model
llm = Ollama(model="llama3.2")  # change to "llama3.2" if you've pulled that version

# Define prompt template
prompt = PromptTemplate.from_template(
    """You are an AI assistant trained using Ollama by Muhammad Anis.

If the user asks about your name or who created you, respond with:
"I was trained for Ollama by Muhammad Anis."

Otherwise, answer the user's question clearly and helpfully.

User: {question}
Answer:"""
)

# Build the chain
chain = LLMChain(prompt=prompt, llm=llm)

# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="Ollama Chatbot - Muhammad Anis", layout="centered")
st.title("🤖 Ollama Chatbot (by Muhammad Anis)")

# Initialize conversation state
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar: conversation history
with st.sidebar:
    st.header("📜 Conversation History")
    if st.session_state.history:
        for i, (q, a) in enumerate(reversed(st.session_state.history)):
            st.markdown(f"**You:** {q}")
            st.markdown(f"**Bot:** {a}")
    else:
        st.markdown("No conversation yet.")
    if st.button("🔁 Reset Conversation"):
        st.session_state.history = []
        st.experimental_rerun()

# Main input area
user_input = st.text_input("Ask me something:", placeholder="Type your question here...")

if st.button("Send") and user_input.strip():
    response = chain.invoke({"question": user_input})
    bot_reply = response["text"]

    # Save to history
    st.session_state.history.append((user_input, bot_reply))

# Show latest reply
if st.session_state.history:
    last_q, last_a = st.session_state.history[-1]
    st.subheader("📝 Response")
    st.markdown(f"**You asked:** {last_q}")
    st.markdown(f"**AI replied:** {last_a}")
