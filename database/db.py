import os

import firebase_admin

from firebase_admin import (
    credentials,
    firestore
)

if not firebase_admin._apps:

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    key_path = os.path.join(
    BASE_DIR,
    "firebase",
    "firebase-key.json"
)

    print("Using Firebase Key:", key_path)

    cred = credentials.Certificate(
        key_path
    )

    firebase_admin.initialize_app(
        cred
    )

db = firestore.client()

print("✅ Firebase Connected Successfully")