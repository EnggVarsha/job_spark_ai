import streamlit as st
from utils.auth import login_user


def show_login():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True
            st.session_state.user = user

            st.success(
                f"Welcome {user['name']}"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Credentials"
            )