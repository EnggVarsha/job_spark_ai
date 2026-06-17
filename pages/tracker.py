import streamlit as st

from database.saved_jobs_db import (
    get_saved_jobs,
    delete_saved_job
)

from database.job_tracker_db import (
    get_applications,
    update_status
)


def show_tracker():

    st.title("📋 Application Tracker")

    tab1, tab2 = st.tabs(
        [
            "Saved Jobs",
            "Applications"
        ]
    )

    # -----------------------------
    # SAVED JOBS
    # -----------------------------

    with tab1:

        jobs = get_saved_jobs()

        if jobs:

            for job in jobs:

                st.markdown("---")

                st.subheader(
                    job.get(
                        "title",
                        "No Title"
                    )
                )

                st.write(
                    "🏢 Company:",
                    job.get(
                        "company",
                        "N/A"
                    )
                )

                st.write(
                    "📍 Location:",
                    job.get(
                        "location",
                        "N/A"
                    )
                )

                st.write(
                    "📅 Saved Date:",
                    job.get(
                        "saved_date",
                        "N/A"
                    )
                )

                job_url = job.get(
                    "job_url",
                    ""
                )

                if job_url:

                    st.link_button(
                        "🔗 Open Job",
                        job_url
                    )

                if st.button(
                    "🗑 Remove",
                    key=f"delete_{job['id']}"
                ):

                    delete_saved_job(
                        job["id"]
                    )

                    st.success(
                        "Job Removed"
                    )

                    st.rerun()

        else:

            st.info(
                "No Saved Jobs Yet"
            )

    # -----------------------------
    # APPLICATIONS
    # -----------------------------

    with tab2:

        applications = get_applications()

        if applications:

            for app in applications:

                st.markdown("---")

                st.subheader(
                    app.get(
                        "title",
                        "No Title"
                    )
                )

                st.write(
                    "🏢 Company:",
                    app.get(
                        "company",
                        "N/A"
                    )
                )

                st.write(
                    "📅 Applied Date:",
                    app.get(
                        "applied_date",
                        "N/A"
                    )
                )

                st.write(
                    "📌 Current Status:",
                    app.get(
                        "status",
                        "Applied"
                    )
                )

                job_url = app.get(
                    "job_url",
                    ""
                )

                if job_url:

                    st.link_button(
                        "🔗 View Job",
                        job_url
                    )

                new_status = st.selectbox(
                    "Update Status",
                    [
                        "Applied",
                        "Interview",
                        "Selected",
                        "Rejected"
                    ],
                    key=f"status_{app['id']}"
                )

                if st.button(
                    "Update",
                    key=f"update_{app['id']}"
                ):

                    update_status(
                        app["id"],
                        new_status
                    )

                    st.success(
                        "Status Updated"
                    )

                    st.rerun()

        else:

            st.info(
                "No Applications Yet"
            )