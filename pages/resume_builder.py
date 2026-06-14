import streamlit as st
import re

from database.resume_db import save_resume

import os

from utils.pdf_generator import (
    create_resume_pdf
)
def is_valid_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email)


def is_valid_linkedin(url):

    pattern = r"^https:\/\/(www\.)?linkedin\.com\/.*"

    return re.match(pattern, url)


def is_valid_github(url):

    pattern = r"^https:\/\/(www\.)?github\.com\/.*"

    return re.match(pattern, url)


def show_resume_builder():

    st.title("📄 Professional Resume Builder")

    st.divider()

    st.subheader("👤 Personal Information")

    profile_photo = st.file_uploader(
        "Upload Profile Photo",
        type=["jpg", "jpeg", "png"]
    )

    full_name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    phone = st.text_input(
        "Phone Number"
    )

    location = st.text_input(
        "Location"
    )

    st.divider()

    st.subheader("💼 Professional Information")

    linkedin = st.text_input(
        "LinkedIn URL"
    )

    github = st.text_input(
        "GitHub URL"
    )

    portfolio = st.text_input(
        "Portfolio URL"
    )

    skills = st.text_area(
        "Skills (comma separated)"
    )

    st.divider()

    st.subheader("🎓 Education")

    college = st.text_input(
        "College Name"
    )

    degree = st.text_input(
        "Degree"
    )

    stream = st.text_input(
        "Stream"
    )

    current_year = st.selectbox(
        "Current Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year",
            "Graduate"
        ]
    )

    cgpa = st.text_input(
        "CGPA / Percentage"
    )

    st.divider()

    st.subheader("🚀 Projects")

    projects = st.text_area(
        "Projects"
    )

    st.divider()

    st.subheader("💻 Experience")

    experience = st.text_area(
        "Experience / Internships"
    )

    st.divider()

    st.subheader("🏆 Certifications")

    certifications = st.text_area(
        "Certifications"
    )

    st.divider()

    st.subheader("🎯 Achievements")

    achievements = st.text_area(
        "Achievements"
    )

    st.divider()

    if st.button(
        "Generate Resume"
    ):

        if not is_valid_email(email):

            st.error(
                "Invalid Email"
            )

            return

        if linkedin and not is_valid_linkedin(
            linkedin
        ):

            st.error(
                "Invalid LinkedIn URL"
            )

            return

        if github and not is_valid_github(
            github
        ):

            st.error(
                "Invalid GitHub URL"
            )

            return

        resume_data = {

            "full_name": full_name,
            "email": email,
            "phone": phone,
            "location": location,

            "linkedin": linkedin,
            "github": github,
            "portfolio": portfolio,

            "skills": skills,

            "college": college,
            "degree": degree,
            "stream": stream,
            "current_year": current_year,
            "cgpa": cgpa,

            "projects": projects,
            "experience": experience,
            "certifications": certifications,
            "achievements": achievements
        }

        save_resume(
            resume_data
        )

        st.success(
            "Resume Saved Successfully"
        )

        st.divider()

        st.subheader(
            "📄 Generated Resume"
        )

        resume_text = f"""
# {full_name}

📧 {email}
📱 {phone}
📍 {location}

LinkedIn:
{linkedin}

GitHub:
{github}

Portfolio:
{portfolio}

---------------------------------

SKILLS

{skills}

---------------------------------

EDUCATION

College:
{college}

Degree:
{degree}

Stream:
{stream}

Current Year:
{current_year}

CGPA:
{cgpa}

---------------------------------

PROJECTS

{projects}

---------------------------------

EXPERIENCE

{experience}

---------------------------------

CERTIFICATIONS

{certifications}

---------------------------------

ACHIEVEMENTS

{achievements}
"""

        st.text_area(
            "Resume Preview",
            resume_text,
            height=600
        )

        st.download_button(
            "⬇ Download Resume",
            resume_text,
            file_name="resume.txt"
        )