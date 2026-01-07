from bson import ObjectId
from datetime import datetime, UTC
import os
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI")
# $env:MONGO_URI="mongodb://localhost:27017"
if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable not set")

client = MongoClient(MONGO_URI)
db = client.notes_app
notes_collection = db.notes



def _note_to_dict(note):
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "content": note["content"],
        "created_at": note["created_at"]
    }


def get_all_notes():
    notes = []
    for note in notes_collection.find().sort("created_at", -1):
        notes.append(_note_to_dict(note))
    return notes


def get_note(note_id):
    note = notes_collection.find_one({"_id": ObjectId(note_id)})
    if not note:
        return None
    return _note_to_dict(note)


def create_note(title, content):
    note = {
        "title": title,
        "content": content,
        "created_at": datetime.now(UTC)
    }
    result = notes_collection.insert_one(note)
    return get_note(str(result.inserted_id))


def update_note(note_id, title, content):
    result = notes_collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {"title": title, "content": content}}
    )
    if result.matched_count == 0:
        return None
    return get_note(note_id)


def delete_note(note_id):
    result = notes_collection.delete_one({"_id": ObjectId(note_id)})
    return result.deleted_count == 1
