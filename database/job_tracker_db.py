from database.db import db


def save_application(application_data):

    db.collection(
        "applications"
    ).add(application_data)


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

    return len(list(docs))


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