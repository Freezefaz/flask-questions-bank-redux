# from flask import Flask, render_template, redirect, request, url_for

# need to keep to 80 characters, keep the bracket to ensure the identation is kept
from flask import (Flask, render_template, request,
                   redirect, url_for, flash)
import os
import json
# to create a random generator id for python
import uuid
# functions related to sightings are stored in another .py
import sightings
# to allow secret key to be stored in .env file
# pip3 install python-dotenv INSTALL THIS FIRST!
from dotenv import load_dotenv

# Fundamentals of back end programming
# Create
# Read
# Update
# Delete

# to load the secret key that is in the .env file
load_dotenv()

app = Flask(__name__)
# secret key is stored in a .env file and need to create gitignore file to prevent the .env from getting pushed
app.secret_key = os.environ.get('secret_key')

# Make it into dictionary to make it easier to update the radio in html
ufo_shapes = {
    "cigar": "Cigar shaped",
    "saucer": "Suacer shaped",
    "ball": "Ball shaped",
    "others": "Other shapes"
}

# global variable
# coz the sightings are in another .py
database = sightings.load()


@app.route('/')
def show_all_sightings():
    return render_template("all_sightings.template.html", database=database)
# For display form results, need to define sighting and ufo shapes to be used in html


@app.route('/create-sighting')
def show_create_sighting_form():
    return render_template("sighting_form.template.html", sighting={},
                           ufo_shapes=ufo_shapes)


# To create get the form info
@app.route('/create-sighting', methods=["POST"])
def process_create_sighting_form():
    # uuid needs to be a string coz its at html
    next_id = str(uuid.uuid1())
    # because the import sightings every function related to sightings need to have sightings.
    sighting = sightings.create_sighting(next_id, request)
    # set key for each sighting
    database[next_id] = sighting
    sightings.save(database)
    # get feedback for each changes made during update and delete
    flash(f"ID added: {next_id}")
    flash(f"New sighting created: {request.form.get('title')}")

    return redirect(url_for("show_all_sightings"))

# to edit the reports and id has to be string coz of html


@app.route('/edit-sighting/<sighting_id>')
def show_edit_sighting_form(sighting_id):
    # database[sighting_id] can also be used but there was an issue
    sighting = database.get(sighting_id)
    # to prevent system from crashing if the id is not found
    if sighting is None:
        return "Not found. ID does not exist"

    return render_template('edit_sighting.template.html', sighting=sighting,
                           ufo_shapes=ufo_shapes)


# to edit the reports and id has to be string coz of html
@app.route('/edit-sighting/<sighting_id>', methods=["POST"])
def edit_sighting(sighting_id):
    # to prevent system from crashing if the id is not found
    sighting = sightings.get_by_id(database, sighting_id)
    if sighting is None:
        return "Not found. ID does not exist"
    # to get the values from forms and create each report
    sighting = sightings.create_sighting(sighting_id, request)
    # to give key to each sighting report
    database[sighting_id] = sighting
    # save sighting report changes to the database
    sightings.save(database)
    # show changes to user when an edit is made
    flash(f"Sighting with the id of {sighting_id} has been modified")

    return redirect(url_for("show_all_sightings"))

# to delete past sighting reports


@app.route('/delete-sighting/<sighting_id>')
def show_delete_confirmation(sighting_id):
    # sighting = database.get(sighting_id)
    sighting = database[sighting_id]
    return render_template("confirm_to_delete.template.html",
                           sighting=sighting)

# # to delete past sighting reports and show on the all reports display page


@app.route('/delete-sighting/<sighting_id>', methods=["POST"])
def process_delete(sighting_id):
    # assign vairable
    sighting = database.get(sighting_id)
    # delete the specific report
    del database[sighting_id]
    # save changes to the database
    sightings.save(database)
    # show which report was deleted from the database to user
    flash(f"Sighting titled {sighting['title']} has been deleted")
    return redirect(url_for("show_all_sightings"))

# Must be at the start to work
def save():
    with open("db.json", "w") as fileptr:
        json.dump(database, fileptr)


def load():
    database = {}  # Python not needed but for consistent with javscript
    with open("db.json", "r") as fileptr:
        # only need 1 arguement
        database = json.load(fileptr)
        return database

# ***** ITERATE DICTIONARY IS NOT EFFICIENT AS THE KEYS ARE NOT SORTED BETTER TO USE A LIST ******


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
