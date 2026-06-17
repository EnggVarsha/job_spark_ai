from firebase_admin import firestore

db = firestore.client()


def save_job(job_data):

    title = job_data.get("title", "")
    company = job_data.get("company", "")

    doc_id = f"{title}_{company}"

    existing = (
        db.collection("saved_jobs")
        .document(doc_id)
        .get()
    )

    if existing.exists:
        return False

    db.collection(
        "saved_jobs"
    ).document(
        doc_id
    ).set(
        job_data
    )

    return True


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


def delete_saved_job(job_id):

    db.collection(
        "saved_jobs"
    ).document(
        job_id
    ).delete()


def is_job_saved(
    title,
    company
):

    doc_id = f"{title}_{company}"

    doc = (
        db.collection("saved_jobs")
        .document(doc_id)
        .get()
    )

    return doc.exists


def get_saved_job(job_id):

    doc = (
        db.collection("saved_jobs")
        .document(job_id)
        .get()
    )

    if doc.exists:

        data = doc.to_dict()

        data["id"] = doc.id

        return data

    return None