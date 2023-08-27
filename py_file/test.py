import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("..\FireBase+FastAPI\py_file\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # initialize firestore client


docs = db.collection("users").get()
for doc in docs:
    print(doc.to_dict())
