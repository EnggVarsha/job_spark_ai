from database.db import db


def save_resume(resume_data):

    db.collection(
        "resumes"
    ).add(
        resume_data
    )


def get_resumes():

    docs = db.collection(
        "resumes"
    ).stream()

    resumes = []

    for doc in docs:

        data = doc.to_dict()

        data["id"] = doc.id

        resumes.append(data)

    return resumes