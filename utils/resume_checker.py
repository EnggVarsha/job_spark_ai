def check_resume_sections(text):

    text = text.lower()

    sections = {
        "Education": "education" in text,
        "Skills": "skills" in text,
        "Projects": "project" in text,
        "Internship": "internship" in text,
        "Experience": "experience" in text,
        "Certification": "certification" in text
    }

    return sections