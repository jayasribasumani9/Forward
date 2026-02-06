from pymongo import MongoClient

MONGO_URI="mongodb+srv://jayasribasumani9_db_user:kpfPsPPhqnO9jC5M@cluster0.z36uydc.mongodb.net/?appName=Cluster0"

client= MongoClient(MONGO_URI)

db = client["notes_db"]
notes_collection=db["notes"]