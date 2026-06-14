import streamlit as st

from database.saved_jobs_db import (
    get_saved_jobs_count
)

from database.job_tracker_db import (
    get_applications_count
)


def show_dashboard():

    saved_jobs = get_saved_jobs_count()

    applications = get_applications_count()

    st.title("🚀 JobSpark AI")

    st.subheader(
        "Your AI Career Copilot"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Jobs Found",
            "0"
        )

    with col2:
        st.metric(
            "Applications",
            applications
        )

    with col3:
        st.metric(
            "ATS Score",
            "75"
        )

    with col4:
        st.metric(
            "Saved Jobs",
            saved_jobs
        )

    st.divider()

    st.subheader(
        "👤 Profile"
    )

    if "user" in st.session_state:

        user = st.session_state.user

        st.write(
            f"**Name:** {user.get('name','N/A')}"
        )

        st.write(
            f"**Email:** {user.get('email','N/A')}"
        )

        st.write(
            f"**Skills:** {user.get('skills','Not Added')}"
        )

    st.divider()

    st.info(
        """
✔ AI Chatbot

✔ Job Search

✔ Resume Builder

✔ Resume Analyzer

✔ Application Tracker
"""
    )