from database.db import db


def save_profile(profile_data):

    email = profile_data["email"]

    db.collection(
        "profiles"
    ).document(
        email
    ).set(
        profile_data
    )


def get_profile(email):

    doc = db.collection(
        "profiles"
    ).document(
        email
    ).get()

    if doc.exists:

        return doc.to_dict()

    return {}