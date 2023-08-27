import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("Firebase+Python/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()  # initialize firestore client

data={"name": "John", "age": 30, "city": "Sri Lanka", "state": "NY", "country": "USA", "hobbies": ["hiking", "biking", "skiing"], "is_active": True}

#   ************************************** add document to collection with auto generated id**************************************

db.collection("users").add(data) # add data to firestore

# **************************************** add document to collection with custom id ****************************************

# db.collection("users").document("johnNewYork").set(data) 

#       using .document we can add data without data duplication

# **************************************** merge/update data to existing document data to existing document ****************************************

# db.collection("users").document("johnNewYork").set({"univercity":"UOM"}, merge=True)

# **************************************** add Sub collection  ****************************************

# db.collection("users").document("johnNewYork").collection("Subject").add({"name":"Maths","marks":90})
db.collection("users").document("johnNewYork").collection("Subject").document("sem1").set({"name":"Maths","marks":90})



