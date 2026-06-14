from database.db import db


def save_job(job_data):

    db.collection(
        "saved_jobs"
    ).add(job_data)


def get_saved_jobs():

    docs = db.collection(
        "saved_jobs"
    ).stream()

    jobs = []

    for doc in docs:

        data = doc.to_dict()

        data["id"] = doc.id

        jobs.append(data)

    return jobs


def get_saved_jobs_count():

    docs = db.collection(
        "saved_jobs"
    ).stream()

    return len(list(docs))