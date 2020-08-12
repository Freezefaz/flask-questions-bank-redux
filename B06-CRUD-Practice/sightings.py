import json

# this is to store sightings related functions and whatnot
# so since its on a different .py need to keep in arguements into the functions

# make the sighting into a dictionary
def create_sighting(next_id, request):
    sighting = {
        "id": next_id,
        "title": request.form.get('title'),
        "email": request.form.get("email"),
        "shape_category": request.form.get("shape-category"),
        "other-shape": request.form.get('other-shape'),
        "lat": request.form.get("lat"),
        "lng": request.form.get("lng"),
        "description": request.form.get('comments')
    }
    return sighting

# to save to json
def save(database):
    with open("db.json", "w") as fileptr:
        json.dump(database, fileptr)

# to retrieve database
def load():
    database = {}
    with open("db.json", "r") as fileptr:
        database = json.load(fileptr)
    return database

# assign the unique id to each report
def get_by_id(database, sighting_id):
    return database.get(sighting_id)