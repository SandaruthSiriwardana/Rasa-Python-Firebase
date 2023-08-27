import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# setup
cred = credentials.Certificate("Firebase+Python/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()  # initialize firestore client


# ****************** delete using know document id ******************

"""db.collection("users").document("d1").delete()"""

# ****************** know id -field  ******************

"""db.collection("users").document("d2").update({"school": firestore.DELETE_FIELD})"""

# ****************** unkown id  ******************

# first way

"""docs=db.collection("users").get()
for doc in docs:
    data = doc.to_dict()
    if 'neme' in data and data['neme'] == "kavindu":
        key=doc.id
        db.collection("users").document(key).delete()"""

# second way (using where clause)

"""docs=db.collection("users").where(filter = FieldFilter("name", "==", "sada")).get()
for doc in docs:
    key=doc.id
    db.collection("users").document(key).delete()"""

# ****************** delete multiple fields in unkow id  ******************
"""docs=db.collection("users").where(filter = FieldFilter("age", "==", 44)).get()
for doc in docs:
    key=doc.id
    db.collection("users").document(key).update({"city": firestore.DELETE_FIELD , "name": firestore.DELETE_FIELD})"""

# ****************** delete all data ******************

docs=db.collection("users").get()
for doc in docs:
    key=doc.id
    db.collection("users").document(key).delete()