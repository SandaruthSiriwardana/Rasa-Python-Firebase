import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# setup
cred = credentials.Certificate("Firebase+Python/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()  # initialize firestore client

# ****************** update using know document id ******************

"""db.collection("users").document("johnNewYork").update({"age": 40})"""

# update intiger value using increment

"""db.collection("users").document("johnNewYork").update({"age": firestore.Increment(2)})"""

# use update to add new field(update not existing field)

"""not_existing_field = "newField"
db.collection("users").document("johnNewYork").update({not_existing_field: "new value"})
db.collection("users").document("d1").update({"Books":["book1","book2","book3"]}) """

# array update(append and remove)

"""db.collection("users").document("d1").update({"hobbies": firestore.ArrayUnion(["eating", "sleeping"])})

db.collection("users").document("d1").update({"hobbies": firestore.ArrayRemove(["eating"])})
"""

# ****************** unkown id  ******************
# first way

docs=db.collection("users").get()
"""for doc in docs:
    data = doc.to_dict()
    if 'age' in data and data['age'] >= 40:
        key=doc.id
        db.collection("users").document(key).update({"age_group":"old"})"""

# second way (using where clause)

docs=db.collection("users").where(filter = FieldFilter("age", ">=", 40)).get()
for doc in docs:
    key=doc.id
    db.collection("users").document(key).update({"age_group":"older than 40"})