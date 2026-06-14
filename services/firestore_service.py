from database.db import db


def add_application(data):

    db.collection(
        "applications"
    ).add(data)


def get_applications():

    docs = db.collection(
        "applications"
    ).stream()

    applications = []

    for doc in docs:

        item = doc.to_dict()

        item["id"] = doc.id

        applications.append(item)

    return applications


def delete_application(doc_id):

    db.collection(
        "applications"
    ).document(
        doc_id
    ).delete()