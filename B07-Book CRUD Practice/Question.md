Book CRUD

Create a new Flask app inside app.py (important: for the automated marking to work, it must be app.py)

A book has the following fields:

{
    "isbn":"X123-456",
    "title":"The Lord of the Rings",
    "type":"non-fiction",
    "genre":"fantasy",
    "tags":["page-turner", "poetic", "doorstopper"],
    "author":"J.R.R Tolkien",
    "synospis":"A halfing must destroy stolen jewellery"
}

Some Notes:

    The ISBN of a book is always unique.
    Type can be non-fiction or fiction
    Genre can be fantasy, science-fic, romance or slice-of-life
    Tags is a list, and there is no fixed list

Add in the following routes:
/

Display all the books in the system using in an unodered list (using <ul>), with the book title in each list item (<li></li>)
GET /search

Create a form that allows the user to search for a book by title.
POST /search

Display books that match the user's query that they entered in POST /search
GET /add

Displays the form that allows the user to add in a book.
POST /add

Process the form that allows the user to add in a book (from GET /add). Before adding, make sure the book's ISBN is unique. Redirect back to / with a flash message when done.
GET /edit/

Display a form which allows the user to modify the details of a book specified by the ISBN
POST /edit/

Modify the details of a book specified by the ISBN. Redirect back to / with a flash message when done.
GET /choose_delete

Display a list of books. Allow the user to select one to delete.
GET /delete_book/

Confirm with the user if they wish to delete a book specified by the ISBN
POST /delete_book/

Delete the book specified by the ISBN. Redirect back to / with a flash message when done.