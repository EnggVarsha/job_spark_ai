from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_resume_pdf(
    file_path,
    resume_data
):

    doc = SimpleDocTemplate(
        file_path
    )

    styles = getSampleStyleSheet()

    content = []

    # -----------------------------
    # HEADER
    # -----------------------------

    content.append(
        Paragraph(
            f"<b>{resume_data.get('full_name','')}</b>",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # CONTACT DETAILS
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Contact Information</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Email: {resume_data.get('email','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Phone: {resume_data.get('phone','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Location: {resume_data.get('location','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"LinkedIn: {resume_data.get('linkedin','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"GitHub: {resume_data.get('github','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # PROFESSIONAL SUMMARY
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Professional Summary</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "summary",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # SKILLS
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Skills</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "skills",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # EDUCATION
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Education</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"College: {resume_data.get('college','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Degree: {resume_data.get('degree','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Stream: {resume_data.get('stream','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Current Year: {resume_data.get('current_year','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"CGPA / Percentage: {resume_data.get('cgpa','')}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # PROJECTS
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Projects</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "projects",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # EXPERIENCE
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Experience</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "experience",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # CERTIFICATIONS
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Certifications</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "certifications",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # ACHIEVEMENTS
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Achievements</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "achievements",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # -----------------------------
    # LANGUAGES
    # -----------------------------

    content.append(
        Paragraph(
            "<b>Languages</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume_data.get(
                "languages",
                ""
            ),
            styles["BodyText"]
        )
    )

    # -----------------------------
    # BUILD PDF
    # -----------------------------

    doc.build(content)