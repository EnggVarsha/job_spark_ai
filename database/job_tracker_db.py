from database.db import db


def save_application(application_data):

    db.collection(
        "applications"
    ).add(
        application_data
    )


def get_applications():

    docs = db.collection(
        "applications"
    ).stream()

    applications = []

    for doc in docs:

        data = doc.to_dict()

        data["id"] = doc.id

        applications.append(data)

    return applications


def get_applications_count():

    docs = db.collection(
        "applications"
    ).stream()

    return len(
        list(docs)
    )


def get_selected_jobs_count():

    docs = db.collection(
        "applications"
    ).stream()

    count = 0

    for doc in docs:

        data = doc.to_dict()

        if data.get(
            "status",
            ""
        ) == "Selected":

            count += 1

    return count


def get_rejected_jobs_count():

    docs = db.collection(
        "applications"
    ).stream()

    count = 0

    for doc in docs:

        data = doc.to_dict()

        if data.get(
            "status",
            ""
        ) == "Rejected":

            count += 1

    return count


def get_pending_jobs_count():

    docs = db.collection(
        "applications"
    ).stream()

    count = 0

    for doc in docs:

        data = doc.to_dict()

        if data.get(
            "status",
            ""
        ) == "Pending":

            count += 1

    return count


def update_status(
    application_id,
    new_status
):

    db.collection(
        "applications"
    ).document(
        application_id
    ).update(
        {
            "status": new_status
        }
    )


def delete_application(
    application_id
):

    db.collection(
        "applications"
    ).document(
        application_id
    ).delete()