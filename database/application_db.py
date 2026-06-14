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


def update_status(app_id, status):

    db.collection(
        "applications"
    ).document(
        app_id
    ).update(
        {
            "status": status
        }
    )