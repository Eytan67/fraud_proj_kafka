from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost:27018/'
DB_NAME = 'potential_fraud_transactions'

def get_mongo_connection(collection_name):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]

    return db[collection_name]


# try:
#     db, client = get_mongo_connection()
#     # ניסיון לקרוא את שם המסד והאוסף
#     print("Database names:", client.list_database_names())  # רשימת כל המסדים
#     print("Collection names in db:", db.list_collection_names())  # רשימת האוספים במסד הנוכחי
#
#     # בדיקה ספציפית לאוסף שהוגדר
#     if COLLECTION_NAME in db.list_collection_names():
#         print(f"Connection successful! Collection '{COLLECTION_NAME}' exists in database '{DB_NAME}'.")
#     else:
#         print(f"Connected to '{DB_NAME}', but collection '{COLLECTION_NAME}' does not exist.")
# except Exception as e:
#     print("Failed to connect to MongoDB:", e)
# finally:
#     client.close()