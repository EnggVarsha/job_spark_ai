import streamlit as st
import pandas as pd
import plotly.express as px

from database.saved_jobs_db import (
    get_saved_jobs_count
)

from database.job_tracker_db import (
    get_applications_count,
    get_selected_jobs_count
)


def show_dashboard():

    saved_jobs = get_saved_jobs_count()

    applications = get_applications_count()

    selected_jobs = get_selected_jobs_count()

    ats_score = st.session_state.get(
        "ats_score",
        None
    )

    st.title("🚀 JobSpark AI Dashboard")

    if "user" in st.session_state:

        user = st.session_state.user

        st.markdown(
            f"""
            ### Welcome, {user.get('name','User')} 👋

            Your AI Career Copilot
            """
        )

    st.write("")

    # -----------------------------
    # TOP METRIC CARDS
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📂 Saved Jobs",
            saved_jobs
        )

    with col2:

        st.metric(
            "📝 Applications",
            applications
        )

    with col3:

        st.metric(
            "🏆 Selected Jobs",
            selected_jobs
        )

    with col4:

        st.metric(
            "📊 ATS Score",
            ats_score if ats_score else "Not Checked"
        )

    st.divider()

    # -----------------------------
    # CHARTS
    # -----------------------------

    left, right = st.columns(2)

    with left:

        st.subheader(
            "📈 Application Status"
        )

        chart_data = pd.DataFrame(
            {
                "Status": [
                    "Applied",
                    "Selected",
                    "Pending"
                ],
                "Count": [
                    applications,
                    selected_jobs,
                    max(
                        applications - selected_jobs,
                        0
                    )
                ]
            }
        )

        fig = px.bar(
            chart_data,
            x="Status",
            y="Count",
            title="Applications Overview"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader(
            "🛠 Skills Distribution"
        )

        if "user" in st.session_state:

            skills = user.get(
                "skills",
                ""
            )

            if skills:

                skill_list = [
                    s.strip()
                    for s in skills.split(",")
                    if s.strip()
                ]

                if len(skill_list) > 0:

                    skill_df = pd.DataFrame(
                        {
                            "Skill": skill_list,
                            "Value": [1] * len(skill_list)
                        }
                    )

                    pie_fig = px.pie(
                        skill_df,
                        names="Skill",
                        values="Value"
                    )

                    st.plotly_chart(
                        pie_fig,
                        use_container_width=True
                    )

                else:

                    st.info(
                        "No skills added."
                    )

            else:

                st.info(
                    "Update your profile to see skills analytics."
                )

    st.divider()

    # -----------------------------
    # PROFILE SUMMARY
    # -----------------------------

    st.subheader(
        "👤 Profile Summary"
    )

    if "user" in st.session_state:

        st.write(
            f"**Name:** {user.get('name','N/A')}"
        )

        st.write(
            f"**Email:** {user.get('email','N/A')}"
        )

        st.write(
            f"**Skills:** {user.get('skills','Not Added')}"
        )

        if st.button(
            "👤 View Profile"
        ):

            st.session_state["dashboard_to_profile"] = True

            st.info(
                "Open Profile tab from sidebar."
            )

    st.divider()

    # -----------------------------
    # RECENT ACTIVITY
    # -----------------------------

    st.subheader(
        "📜 Activity Summary"
    )

    st.success(
        f"Saved Jobs: {saved_jobs}"
    )

    st.success(
        f"Applications: {applications}"
    )

    st.success(
        f"Selected Jobs: {selected_jobs}"
    )

    if ats_score:

        st.success(
            f"Latest ATS Score: {ats_score}"
        )

    else:

        st.warning(
            "Resume not analyzed yet. Use Resume Analyzer to generate ATS score."
        )

    st.divider()

    # -----------------------------
    # QUICK ACTIONS
    # -----------------------------

    st.subheader(
        "⚡ Quick Actions"
    )

    a, b, c = st.columns(3)

    with a:

        st.info(
            "🔍 Search Jobs"
        )

    with b:

        st.info(
            "📄 Build Resume"
        )

    with c:

        st.info(
            "📊 Analyze Resume"
        )