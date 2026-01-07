async function loadNotes() {
    const res = await fetch("/api/notes");
    const notes = await res.json();

    const list = document.getElementById("notes-list");
    list.innerHTML = "";

    notes.forEach(note => {
        const li = document.createElement("li");
        li.textContent = note.title;
        li.onclick = () => {
            window.location.href = `/notes/${note.id}`;
        };
        list.appendChild(li);
    });
}

function createNewNote() {
    window.location.href = "/notes/new";
}

loadNotes();

const pathParts = window.location.pathname.split("/");
const noteId = pathParts[pathParts.length - 1];

const isNew = noteId === "new";

async function loadNote() {
    if (isNew) {
        document.getElementById("page-title").textContent = "New Note";
        return;
    }

    const res = await fetch(`/api/notes/${noteId}`);
    if (!res.ok) return;

    const note = await res.json();
    document.getElementById("title").value = note.title;
    document.getElementById("content").value = note.content;
}

async function saveNote() {
    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    if (!title || !content) {
        alert("Title and content required");
        return;
    }

    const payload = { title, content };

    if (isNew) {
        await fetch("/api/notes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
    } else {
        await fetch(`/api/notes/${noteId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
    }

    window.location.href = "/";
}

async function deleteNote() {
    if (isNew) return;

    const confirmed = confirm("Delete this note?");
    if (!confirmed) return;

    await fetch(`/api/notes/${noteId}`, {
        method: "DELETE"
    });

    window.location.href = "/";
}

function goBack() {
    window.location.href = "/";
}

if (window.location.pathname.startsWith("/notes")) {
    loadNote();
}
