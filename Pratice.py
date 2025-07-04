import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama


# Initialize Ollama LLM
llm = Ollama(model="llama3.2")  # Use "llama3" instead of "llama3.2" if that model name doesn't exist

# Prompt Template
prompt = PromptTemplate.from_template(
    """You are an AI assistant trained using Ollama by Muhammad Anis.

If the user asks about your name or who created you, respond with:
"I was trained for Ollama by Muhammad Anis."

Otherwise, answer the user's question clearly and helpfully.

User: {question}
Answer:"""
)

# Streamlit UI setup
st.set_page_config(page_title="Muhammad Anis | Ollama Chatbot")
st.title("🤖 Ollama Chatbot (Muhammad Anis)")

# Initialize session state for conversation
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar conversation history
with st.sidebar:
    st.header("🕘 Conversation History")
    for i, (q, a) in enumerate(reversed(st.session_state.history)):
        st.markdown(f"**Q{i+1}:** {q}")
        st.markdown(f"*A{i+1}:* {a}")
    if st.button("🔁 Reset Conversation"):
        st.session_state.history = []
        st.experimental_rerun()

# Main input/output area
user_input = st.text_input("Ask me anything:", placeholder="Type your question here...")

if st.button("Submit") and user_input:
    formatted_prompt = prompt.format(question=user_input)
    response = llm.invoke(formatted_prompt)
    st.session_state.history.append((user_input, response))

# Display latest answer
if st.session_state.history:
    last_question, last_answer = st.session_state.history[-1]
    st.subheader("📝 Response")
    st.markdown(f"**You asked:** {last_question}")
    st.markdown(f"**AI answered:** {last_answer}")
