import streamlit as st

from database.saved_jobs_db import (
    get_saved_jobs
)

from database.job_tracker_db import (
    get_applications,
    update_status
)


def show_tracker():

    st.title(
        "📋 Application Tracker"
    )

    tab1, tab2 = st.tabs(
        [
            "Saved Jobs",
            "Applications"
        ]
    )

    # ---------------------
    # SAVED JOBS
    # ---------------------

    with tab1:

        jobs = get_saved_jobs()

        if jobs:

            for job in jobs:

                st.info(
                    f"{job.get('title','N/A')} | "
                    f"{job.get('company','N/A')}"
                )

        else:

            st.warning(
                "No Saved Jobs"
            )

    # ---------------------
    # APPLICATIONS
    # ---------------------

    with tab2:

        applications = get_applications()

        if applications:

            for app in applications:

                st.subheader(
                    app.get(
                        "title",
                        "No Title"
                    )
                )

                st.write(
                    app.get(
                        "company",
                        "No Company"
                    )
                )

                st.write(
                    "Status:",
                    app.get(
                        "status",
                        "Applied"
                    )
                )

                new_status = st.selectbox(
                    "Update Status",
                    [
                        "Applied",
                        "Interview",
                        "Selected",
                        "Rejected"
                    ],
                    key=app["id"]
                )

                if st.button(
                    "Update",
                    key=f"btn_{app['id']}"
                ):

                    update_status(
                        app["id"],
                        new_status
                    )

                    st.success(
                        "Status Updated"
                    )

                st.divider()

        else:

            st.warning(
                "No Applications Yet"
            )