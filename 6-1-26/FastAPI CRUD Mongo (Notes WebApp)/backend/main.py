from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pydantic import BaseModel

from backend.mongo_notes import (
    get_all_notes,
    get_note,
    create_note,
    update_note,
    delete_note
)


app = FastAPI(title="Notes Web App")
app.mount("/static", StaticFiles(directory="frontend"), name="static")


class NoteCreate(BaseModel):
    title: str
    content: str


@app.get("/api/notes")
def api_get_notes():
    return get_all_notes()


@app.get("/api/notes/{note_id}")
def api_get_note(note_id: str):
    note = get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.post("/api/notes")
def api_create_note(note: NoteCreate):
    return create_note(note.title, note.content)


@app.put("/api/notes/{note_id}")
def api_update_note(note_id: str, note: NoteCreate):
    updated = update_note(note_id, note.title, note.content)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated


@app.delete("/api/notes/{note_id}")
def api_delete_note(note_id: str):
    success = delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"status": "deleted"}


@app.get("/", response_class=HTMLResponse)
def notes_list_page():
    with open("frontend/notes_list.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/notes/new", response_class=HTMLResponse)
def new_note_page():
    with open("frontend/notes_edit.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/notes/{note_id}", response_class=HTMLResponse)
def edit_note_page(note_id: str):
    with open("frontend/notes_edit.html", "r", encoding="utf-8") as f:
        return f.read()
