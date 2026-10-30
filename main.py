from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def root_mess():
    return{f"Любимая книга {book}"}

book =""


class BookCreate(BaseModel):
    book: str

@app.post("/book", status_code = status.HTTP_201_CREATED)
def set_book(payload: BookCreate):
    global book
    book = payload.book
    return {"message": "книга сохранена"}
