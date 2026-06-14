import streamlit as st
from agents.chatbot_agent import career_chat


def show_chatbot():

    st.title("🤖 JobSpark AI Career Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    prompt = st.chat_input(
        "Ask career questions..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner(
            "Thinking..."
        ):

            reply = career_chat(prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        with st.chat_message(
                "assistant"
        ):
            st.markdown(reply)