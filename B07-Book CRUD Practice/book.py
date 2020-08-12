import json
import uuid

def new_isbn():
    isbn = str(uuid.uuid4())
    return isbn

def create_book(book_id, request):
    book = {
        "id": book_id,
        "isbn": new_isbn(),
        "title": request.form.get("title"),
        "book_type": request.form.get("book_type"),
        "genre": request.form.get("genre"),
        "tags": request.form.get("tags"), #can add a split() to make it a list AND use join() to publish
        "author": request.form.get("author"),
        "synopsis": request.form.get("synopsis")
    }
    return book

def save(database):
    with open("db.json", "w") as fileptr:
        json.dump(database, fileptr)

def load():
    database = {}
    with open("db.json", "r") as fileptr:
        database = json.load(fileptr)
    return database