
import streamlit as st
from rag import ask_question

st.set_page_config(
    page_title="Company RAG Assistant",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Company RAG Assistant")
st.caption("Ask questions about company documents.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("About")
    st.write(
        "This assistant uses Google Gemini and ChromaDB "
        "to answer questions from company documents."
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask about company policies...")

if question:
    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            try:
                answer = ask_question(question)
            except Exception as e:
                print(f"Error: {e}")
                answer = (
                    "Something went wrong. Please check "
                    "your API configuration and ChromaDB."
                )

        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
