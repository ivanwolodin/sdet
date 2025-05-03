from fastapi import FastAPI, HTTPException, Form
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env-test")

app = FastAPI()


@app.get("/api/main")
async def main():
    return {"message": "ok"}


@app.post("/api/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == os.getenv("LOGIN") and password == os.getenv("PASSWORD"):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
