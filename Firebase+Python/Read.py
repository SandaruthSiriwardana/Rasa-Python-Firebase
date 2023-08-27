import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate("Firebase+Python/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()  # initialize firestore client

#  to get Know the document id

'''users_ref = db.collection("users")
 docs = users_ref.document("johnNewYork")
 if docs.get().exists:
     print("Document data: {}".format(docs.get().to_dict()))    '''

'''result=db.collection("users").document("johnNewYork").get()
if result.exists:
    print(result.to_dict())'''

# get all documents in a collection

"""docs = db.collection("users").get()
for doc in docs:
    print(doc.to_dict())"""

# Querying

# docs = db.collection("users").where("age", "==", 30).get()
# docs = db.collection("users").where("age", ">", 30).get()

# singal where clause
"""docs = db.collection("users").where(filter=FieldFilter("country", "==", "SL")).get()
for doc in docs:
    print(doc.to_dict())"""

# use list data type in where clause
"""docs=db.collection("users").where(filter=FieldFilter("hobbies", "array_contains", "hiking")).get()
for doc in docs:
    print(doc.to_dict())"""

# using in operator

docs = db.collection("users").where(filter=FieldFilter("country", "in", ["SL", "IND","PAK"])).get()
for doc in docs:
    print(doc.to_dict())