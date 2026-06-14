import bcrypt
from database.db import db


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def register_user(
        name,
        email,
        password,
        skills
):

    users_ref = db.collection("users")

    existing = users_ref.where(
        "email",
        "==",
        email
    ).get()

    if existing:
        return False, "Email already exists"

    users_ref.add({
        "name": name,
        "email": email,
        "password": hash_password(password),
        "skills": skills
    })

    return True, "Registration successful"


def login_user(email, password):

    users_ref = db.collection("users")

    docs = users_ref.where(
        "email",
        "==",
        email
    ).get()

    if not docs:
        return None

    user = docs[0].to_dict()

    if verify_password(
            password,
            user["password"]
    ):
        return user

    return None