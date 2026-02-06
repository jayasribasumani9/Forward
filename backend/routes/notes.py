from fastapi import APIRouter, HTTPException
from databse import notes_collection
from models import Note
from bson import ObjectId

router=APIRouter(prefix="/notes",tags=["Note"])

@router.post("/")
def create_notes(note:Note):
    result=notes_collection.insert_one(note.dict())
    return {"id":str(result.inserted_id)}

@router.get("/{note_id}")
def get_note(note_id:str):
    note=notes_collection.find_one({"_id":ObjectId(note_id)})
    note["_id"]=str(note["_id"])
    return note

@router.put("/{notes_id}")
def update_note(note_id:str,note:Note):
    result=notes_collection.update_one(
        {"_id":ObjectId(note_id)},
        {"$set":note.dict(exclude={"created_at"})}
    )

    if result.matched_count==0:
        raise HTTPException(status_code=404,detail="Note Not Found!")
    return {"messsage":"Note updated"}

@router.delete("/{note_id}")
def delete_note(note_id:str):
    notes_collection.delete_one({"_id":ObjectId(note_id)})
    return {"message":"Note deleted"}

@router.get("/notes")
def get_all_notes():
    notes=[]
    for note in notes_collection.find():
        note["_id"]=str(note["_id"])
        notes.append(note)

    return notes
