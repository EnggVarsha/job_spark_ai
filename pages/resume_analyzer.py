import streamlit as st

from services.gemini_service import (
    analyze_resume_ai,
    improve_resume_ai
)

from services.resume_parser import extract_resume_text
from utils.resume_checker import check_resume_sections
from utils.ats_score import calculate_ats_score


def show_resume_analyzer():

    st.title("📊 AI Resume Analyzer")

    st.write(
        "Upload your resume and get ATS analysis, improvement suggestions, and AI recommendations."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "jpg", "jpeg", "png"]
    )

    if uploaded_file:

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_resume_text(
                uploaded_file
            )

        st.success(
            "Analysis Completed Successfully"
        )

        st.subheader(
            "📄 Extracted Resume Text"
        )

        st.write(
            "Characters Extracted:",
            len(resume_text)
        )

        st.text_area(
            "Resume Content",
            resume_text,
            height=250
        )

        if len(resume_text.strip()) > 50:

            # --------------------------
            # Resume Sections
            # --------------------------

            sections = check_resume_sections(
                resume_text
            )

            ats_score = calculate_ats_score(
                sections
            )

            st.divider()

            metric1, metric2 = st.columns(2)

            with metric1:

                st.metric(
                    "ATS Score",
                    f"{ats_score}/100"
                )

            with metric2:

                st.metric(
                    "ATS Friendly",
                    "Yes" if ats_score >= 70 else "Needs Improvement"
                )

            st.divider()

            st.subheader(
                "📂 Resume Sections"
            )

            for section, status in sections.items():

                if status:

                    st.success(
                        f"{section} Found"
                    )

                else:

                    st.warning(
                        f"{section} Missing"
                    )

            # --------------------------
            # AI Analysis
            # --------------------------

            with st.spinner(
                "Generating AI Analysis..."
            ):

                analysis = analyze_resume_ai(
                    resume_text
                )

                suggestions = improve_resume_ai(
                    resume_text
                )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "📋 Resume Analysis"
                )

                st.write(
                    analysis
                )

            with col2:

                st.subheader(
                    "✨ ATS Suggestions"
                )

                st.write(
                    suggestions
                )

        else:

            st.error(
                "No text extracted from resume."
            )