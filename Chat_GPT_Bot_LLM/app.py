import streamlit as st
from main import ask_gpt


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #f7f7f8;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 30px;
}

.response-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-top: 20px;
}

.user-box {
    background-color: #e8f0fe;
    padding: 15px;
    border-radius: 12px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">🤖 My AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask anything and get an AI-powered response</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("⚙️ Settings")

    model = st.selectbox(
        "Select Model",
        [
            "gemini-3-flash-preview",
            "gemini-1.5-flash",
            "gemini-1.5-pro"
        ]
    )

    st.divider()

    st.write("### About")

    st.write(
        "This application uses the Google Gemini API "
        "to generate responses to your questions."
    )


# -----------------------------
# User Input
# -----------------------------
user_input = st.text_area(
    "💬 Your Question",
    placeholder="Ask me anything...",
    height=150
)


# -----------------------------
# Ask Button
# -----------------------------
if st.button("🚀 Ask AI", use_container_width=True):

    if not user_input.strip():

        st.warning("Please enter a question.")

    else:

        # Show user question
        st.markdown(
            f"""
            <div class="user-box">
                <b>👤 You</b>
                <br><br>
                {user_input}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Generate response
        with st.spinner("🤔 AI is thinking..."):

            try:

                answer = ask_gpt(
                    model=model,
                    input=user_input
                )

                st.markdown(
                    """
                    <div class="response-box">
                        <b>🤖 AI Assistant</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write(answer)

            except Exception as e:

                st.error(
                    f"Something went wrong: {str(e)}"
                )