import streamlit as st
from utils.auth import register_user


def show_register():

    st.title("📝 Create Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    skills = st.text_area(
        "Skills (comma separated)"
    )

    if st.button("Register"):

        success, message = register_user(
            name,
            email,
            password,
            skills
        )

        if success:
            st.success(message)

        else:
            st.error(message)