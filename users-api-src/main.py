from fastapi import FastAPI

VERSION = "0.2.0"

app = FastAPI(title="Users API", version=VERSION)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "users-api",
        "version": VERSION
    }

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Awa Diop"},
        {"id": 2, "name": "Koffi Kouadio"},
        {"id": 3, "name": "Moussa Traoré"},
        {"id": 4, "name": "Fatou Ndiaye"}
    ]
