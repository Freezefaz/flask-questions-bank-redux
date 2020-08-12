# from flask import Flask, render_template, redirect, request, url_for

# need to keep to 80 characters, keep the bracket to ensure the identation is kept
from flask import (Flask, render_template, request,
                   redirect, url_for)
import os
import book
# to create a random generator id for python
import uuid


app = Flask(__name__)

# load book info from book.py
database = book.load()

# display all the books that have been added
@app.route("/")
def display():
    return render_template("display_books.template.html", database=database)

# get route for add and have to return the book dictionary to define in html
@app.route("/add")
def search():
    return render_template("form.template.html", book={})

# post route for add
@app.route("/add", methods=["POST"])
def process_search():

    #  not necessary to have a book id if the isbn is already a unique id
    book_id = str(uuid.uuid1())
    books= book.create_book(book_id, request)
    # assign the book id to each book
    database[book_id] = books
    # save the to database
    book.save(database)
    return redirect(url_for("display"))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)