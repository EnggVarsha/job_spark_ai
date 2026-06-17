import streamlit as st
from datetime import datetime

from services.jsearch_service import search_jobs

from database.saved_jobs_db import (
    save_job,
    is_job_saved
)

try:
    from database.job_tracker_db import save_application
except:
    save_application = None


def show_job_search():

    st.title("🔍 AI Job Search")

    # -----------------------------
    # FILTERS
    # -----------------------------

    col_left, col_right = st.columns([4, 1])

    with col_right:

        st.subheader("🎯 Filters")

        city = st.selectbox(
            "City",
            [
                "India",
                "Bangalore",
                "Pune",
                "Mumbai",
                "Hyderabad",
                "Delhi",
                "Chennai",
                "Kolkata",
                "Remote"
            ]
        )

        company_filter = st.text_input(
            "Company Name"
        )

        job_type_filter = st.selectbox(
            "Job Type",
            [
                "All",
                "Full Time",
                "Part Time",
                "Contract",
                "Internship"
            ]
        )

        remote_filter = st.selectbox(
            "Work Mode",
            [
                "Any",
                "Remote",
                "Onsite"
            ]
        )

    # -----------------------------
    # SEARCH AREA
    # -----------------------------

    with col_left:

        query = st.text_input(
            "Search Jobs",
            placeholder="Java Developer"
        )

        if "search_results" not in st.session_state:
            st.session_state.search_results = []

        if st.button(
            "🔍 Search Jobs",
            use_container_width=True
        ):

            with st.spinner(
                "Searching jobs..."
            ):

                st.session_state.search_results = search_jobs(
                    query=query,
                    location=city
                )

    jobs = st.session_state.search_results

    # -----------------------------
    # NO RESULTS
    # -----------------------------

    if not jobs:

        st.info(
            "Search jobs to view results."
        )

        return

    st.success(
        f"{len(jobs)} jobs found"
    )

    # -----------------------------
    # JOB LIST
    # -----------------------------

    for index, job in enumerate(jobs):

        title = str(
            job.get(
                "job_title",
                "N/A"
            )
        )

        company = str(
            job.get(
                "employer_name",
                "N/A"
            )
        )

        city_name = str(
            job.get(
                "job_city",
                ""
            )
        )

        country = str(
            job.get(
                "job_country",
                ""
            )
        )

        location = f"{city_name}, {country}"

        employment_type = str(
            job.get(
                "job_employment_type",
                "N/A"
            )
        )

        is_remote = job.get(
            "job_is_remote",
            False
        )

        description = str(
            job.get(
                "job_description",
                ""
            )
        )

        job_url = str(
            job.get(
                "job_apply_link",
                ""
            )
        )

        # -----------------------------
        # FILTERS
        # -----------------------------

        if company_filter:

            if company_filter.lower() not in company.lower():
                continue

        if job_type_filter != "All":

            if job_type_filter.lower().replace(" ", "") not in employment_type.lower().replace("_", "").replace(" ", ""):
                continue

        if remote_filter == "Remote" and not is_remote:
            continue

        if remote_filter == "Onsite" and is_remote:
            continue

        # -----------------------------
        # JOB CARD
        # -----------------------------

        with st.container():

            st.markdown("---")

            st.subheader(title)

            st.write(
                f"🏢 Company: {company}"
            )

            st.write(
                f"📍 Location: {location}"
            )

            st.write(
                f"💼 Employment Type: {employment_type}"
            )

            st.write(
                f"🌐 Remote: {'Yes' if is_remote else 'No'}"
            )

            if description:

                with st.expander(
                    "View Job Description"
                ):

                    st.write(
                        description[:3000]
                    )

            c1, c2, c3 = st.columns(3)

            # -----------------------------
            # SAVE JOB
            # -----------------------------

            with c1:

                if st.button(
                    "💾 Save Job",
                    key=f"save_{index}"
                ):

                    if is_job_saved(
                        title,
                        company
                    ):

                        st.warning(
                            "Job already saved."
                        )

                    else:

                        save_job(
                            {
                                "title": title,
                                "company": company,
                                "location": location,
                                "job_url": job_url,
                                "saved_date": datetime.now().strftime(
                                    "%d-%m-%Y"
                                )
                            }
                        )

                        st.success(
                            "Job saved successfully."
                        )

            # -----------------------------
            # APPLY LINK
            # -----------------------------

            with c2:

                if job_url:

                    st.link_button(
                        "🚀 Apply Job",
                        job_url
                    )

            # -----------------------------
            # TRACK APPLICATION
            # -----------------------------

            with c3:

                applied = st.checkbox(
                    "Applied",
                    key=f"applied_{index}"
                )

                if applied and save_application:

                    if st.button(
                        "✅ Confirm",
                        key=f"confirm_{index}"
                    ):

                        save_application(
                            {
                                "title": title,
                                "company": company,
                                "location": location,
                                "job_url": job_url,
                                "status": "Applied",
                                "date": datetime.now().strftime(
                                    "%d-%m-%Y"
                                )
                            }
                        )

                        st.success(
                            "Application added."
                        )

                        st.rerun()