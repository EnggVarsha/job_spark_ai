from database.db import db

doc_ref = db.collection(
    "test"
).document(
    "connection"
)

doc_ref.set({
    "message": "Firebase is connected"
})

print("✅ Data inserted successfully")