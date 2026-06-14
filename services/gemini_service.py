import google.generativeai as genai

from config.settings import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(prompt):

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {str(e)}"


def analyze_resume_ai(resume_text):

    prompt = f"""
You are an ATS Resume Analyzer.

IMPORTANT RULES:

- Analyze ONLY the uploaded resume.
- Do NOT compare with other resumes.
- Do NOT compare with senior professionals.
- Assume this is a STUDENT resume.
- Judge based on education, skills, projects, internships, achievements and formatting.
- If Education + Skills + Internship + Projects exist, ATS score should generally be between 70-80.
- Focus on what is PRESENT in the resume.

Provide response in this format:

## ATS Score
Score out of 100

## ATS Friendly
Yes or No

## Resume Summary
Summarize candidate profile.

## Strengths
List strengths found in resume.

## Grammar Issues
Mention only actual grammar mistakes.

## Spelling Issues
Mention only actual spelling mistakes.

## Resume Structure Review
Check section arrangement and readability.

## Final Verdict
Explain whether resume is good for a student profile.

Resume:

{resume_text}
"""

    return ask_gemini(prompt)

def improve_resume_ai(resume_text):

    prompt = f"""
You are an ATS Resume Improvement Expert.

IMPORTANT RULES:

- Do NOT rewrite the entire resume.
- Do NOT generate a new resume.
- Do NOT compare with other resumes.
- Analyze only the uploaded resume.

Provide:

## Sentence Improvements

For each weak sentence:

Replace:
<old sentence>

With:
<better sentence>

## ATS Keyword Suggestions

Suggest keywords related to the candidate's profile.

## Missing Information

Mention only information that is actually missing.

## Formatting Suggestions

Give formatting improvements.

## Profile Picture Review

If resume contains a photo:
- tell whether photo should be brighter,
- clearer,
- professional,
- or can remain unchanged.

## Resume Builder Suggestion

Suggest user can use JobSpark AI Resume Builder
to automatically improve the resume.

Resume:

{resume_text}
"""

    return ask_gemini(prompt)