import streamlit as st

from services.jsearch_service import (
    search_jobs
)

from database.saved_jobs_db import (
    save_job
)

from database.job_tracker_db import (
    save_application
)


def show_job_search():

    st.title("🔍 AI Job Search")

    query = st.text_input(
        "Search Jobs",
        value="Python Developer in India"
    )

    if st.button("Search Jobs"):

        jobs = search_jobs(query)

        st.session_state.jobs = jobs

    if "jobs" not in st.session_state:

        return

    st.write(
        "Jobs Found:",
        len(st.session_state.jobs)
    )

    for index, job in enumerate(
        st.session_state.jobs
    ):

        st.markdown("---")

        title = job.get(
            "job_title",
            "N/A"
        )

        company = job.get(
            "employer_name",
            "N/A"
        )

        city = job.get(
            "job_city",
            ""
        )

        country = job.get(
            "job_country",
            ""
        )

        employment_type = job.get(
            "job_employment_type",
            "N/A"
        )

        remote = job.get(
            "job_is_remote",
            False
        )

        description = job.get(
            "job_description",
            ""
        )

        apply_link = job.get(
            "job_apply_link",
            ""
        )

        # -------------------
        # JOB DETAILS
        # -------------------

        st.subheader(title)

        st.write(
            "🏢 Company:",
            company
        )

        st.write(
            "📍 Location:",
            city,
            country
        )

        st.write(
            "💼 Employment Type:",
            employment_type
        )

        st.write(
            "🌐 Remote:",
            remote
        )

        if description:

            with st.expander(
                "📄 View Job Description"
            ):

                st.write(
                    description
                )

        # -------------------
        # BUTTONS
        # -------------------

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Save Job",
                key=f"save_{index}"
            ):

                save_job(
                    {
                        "title": title,
                        "company": company,
                        "location": f"{city}, {country}",
                        "apply_link": apply_link
                    }
                )

                st.success(
                    "Job Saved Successfully"
                )

        with col2:

            if st.button(
                "🚀 Apply Job",
                key=f"apply_{index}"
            ):

                st.session_state[
                    "selected_job"
                ] = {

                    "title": title,
                    "company": company,
                    "location": f"{city}, {country}",
                    "apply_link": apply_link

                }

    # -------------------
    # APPLY FLOW
    # -------------------

    if "selected_job" in st.session_state:

        st.divider()

        selected = st.session_state[
            "selected_job"
        ]

        st.subheader(
            "🚀 Job Application"
        )

        st.write(
            f"**Job:** {selected['title']}"
        )

        st.write(
            f"**Company:** {selected['company']}"
        )

        st.write(
            "Have you applied?"
        )

        st.link_button(
            "🌐 Open Official Application Page",
            selected["apply_link"]
        )

        applied = st.radio(
            "Application Status",
            [
                "Not Applied Yet",
                "Applied Successfully"
            ]
        )

        if st.button(
            "Submit Application Status"
        ):

            if applied == "Applied Successfully":

                save_application(
                    {
                        "title": selected[
                            "title"
                        ],
                        "company": selected[
                            "company"
                        ],
                        "status": "Applied"
                    }
                )

                st.success(
                    "Application Added Successfully"
                )

            else:

                st.warning(
                    "Application not submitted."
                )

            del st.session_state[
                "selected_job"
            ]

            st.rerun()