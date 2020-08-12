from flask import Flask, render_template, request, redirect, url_for
import os
import requests

app = Flask(__name__)

@app.route("/")
def order():
    return render_template("raw-form.template.html")


@app.route("/", methods=["POST"])
def process_order():
    # Cannot be outside the function
    total = 0
    name = request.form.get("name")
    # for check boxes use getlsit
    appetizer = request.form.getlist("appetizers")
    # need to put in for loop as it is a list to run through everyone
    for value in appetizer:
        if value == "seafood":
            total += 3.00
            print(total)
        elif value == "fries":
            total += 4.50
            print(total)
        else:
            total += 6
            print(total)
    seating = request.form.get("seating")
    if seating == "vip":
        total += 10
        print(total)
    print(total)

    return render_template("raw-form.template.html", name=name, 
        appetizer=", ".join(appetizer), seating=seating, total=total)

# 2nd Method using dictionary for scalability

# appetizer_cost = {
#     "seafood": {
#         "name": "Overpriced chilled seafood",
#         "price": 3.00
#     },
#         "fries": {
#         "name": "Fries Sprinkled with Fake Truffle Powder",
#         "price": 4.50
#     },
#        "salad": {
#         "name": "Minimal Effort Salad",
#         "price": 6.00
#     }
# }

@app.route("/", methods=["POST"])
def process_order_2nd():
    # Cannot be outside the function
    total = 0
    name = request.form.get("name")
    # for check boxes
    appetizer = request.form.getlist("appetizers")



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)