from fastapi import FastAPI

app = FastAPI(title="Users API")

@app.get("/health")
def health():
    return {"status": "ok", "service": "users-api"}

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Awa Diop"},
        {"id": 2, "name": "Koffi Kouadio"},
        {"id": 3, "name": "Moussa Traoré"}
    ]
