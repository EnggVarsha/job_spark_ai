import streamlit as st

from database.profile_db import (
    save_profile,
    get_profile
)


if "edit_profile" not in st.session_state:

    st.session_state.edit_profile = False

def show_profile():

    st.title("👤 My Profile")

    email = st.session_state.user["email"]

    existing_profile = get_profile(
        email
    )

    if existing_profile is None:

        existing_profile = {}

    st.subheader(
        "Personal Information"
    )

    full_name = st.text_input(
        "Full Name",
        value=existing_profile.get(
            "full_name",
            ""
        )
    )

    username = st.text_input(
        "Username",
        value=existing_profile.get(
            "username",
            ""
        )
    )

    phone = st.text_input(
        "Phone Number",
        value=existing_profile.get(
            "phone",
            ""
        )
    )

    city = st.text_input(
        "City",
        value=existing_profile.get(
            "city",
            ""
        )
    )

    st.divider()

    st.subheader(
        "Professional Information"
    )

    linkedin = st.text_input(
        "LinkedIn URL",
        value=existing_profile.get(
            "linkedin",
            ""
        )
    )

    github = st.text_input(
        "GitHub URL",
        value=existing_profile.get(
            "github",
            ""
        )
    )

    portfolio = st.text_input(
        "Portfolio URL",
        value=existing_profile.get(
            "portfolio",
            ""
        )
    )

    skills = st.text_area(
        "Skills",
        value=existing_profile.get(
            "skills",
            ""
        )
    )

    st.divider()

    st.subheader(
        "College Information"
    )

    college = st.text_input(
        "College Name",
        value=existing_profile.get(
            "college",
            ""
        )
    )

    degree = st.text_input(
        "Degree",
        value=existing_profile.get(
            "degree",
            ""
        )
    )

    stream = st.text_input(
        "Stream",
        value=existing_profile.get(
            "stream",
            ""
        )
    )

    current_year = st.selectbox(
        "Current Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    cgpa = st.text_input(
        "CGPA / Percentage",
        value=existing_profile.get(
            "cgpa",
            ""
        )
    )

    st.divider()

    if st.button(
        "💾 Save Profile"
    ):

        profile_data = {

            "full_name": full_name,
            "username": username,
            "email": email,
            "phone": phone,
            "city": city,

            "linkedin": linkedin,
            "github": github,
            "portfolio": portfolio,
            "skills": skills,

            "college": college,
            "degree": degree,
            "stream": stream,
            "current_year": current_year,
            "cgpa": cgpa
        }

        user_id = st.session_state.user["email"]

        save_profile(
    user_id,
    profile_data
)

        st.success(
            "Profile Saved Successfully"
        )

    st.divider()

    st.subheader(
        "Profile Summary"
    )

    st.write(
        f"👤 Name: {full_name}"
    )

    st.write(
        f"📧 Email: {email}"
    )

    st.write(
        f"🏫 College: {college}"
    )

    st.write(
        f"🎓 Degree: {degree}"
    )

    st.write(
        f"💻 Skills: {skills}"
    )