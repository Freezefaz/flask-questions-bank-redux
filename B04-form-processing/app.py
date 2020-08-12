from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# First part of question

@app.route("/about")
def get_about():
    return render_template('about.template.html')

# Method 1
@app.route('/about', methods=["POST"])
def about():
    number = request.form.get("number")
    # can also use if if if statement
    if number == "1":
        picture = "static/1.jpg"
        # return render_template('about.template.html', picture=picture)
        # if
    elif number == "2":
        picture = "static/2.jpg"
        # return render_template('about.template.html', picture=picture)
        # if
    else:
        picture = "static/3.jpg"
        # return render_template('about.template.html', picture=picture)
    return render_template('about.template.html', picture=picture)
    #  can use also only 1 return render_template('about.template.html', picture=picture)

#Method 2 if else statement in the template

@app.route('/about', methods=["POST"])
def second_about():
    number = request.form.get("number")
    number = int(request.form.get("number"))
    return render_template("about.template.html", number=number)


# 2nd Part of question
# For some reason context is undefined so need to find

@app.route('/')
def home():
    # Add context so that when the checkbox is not ticked it can still return the values keyed in form
    # return render_template('form.template.html', context={})
    return render_template('form.template.html')

@app.route("/", methods=["POST"])
def get_home():
    name = request.form.get("name")
    sex = request.form.get("sex")
    comment = request.form.get("comment")
    contact = request.form.get("can-contact")
    # to change the value
    # better to keep boolean value in json for consistency
    if contact == "1":
        contact = "Yes"
    else:
        contact = "No"
    #  need to have a feedback for democheckbox
    accept = request.form.get("democheckbox")
    # agree = request.form["democheckbox"] is faster but if info not available will cause it to crash
    if accept == "yes":
        accept = True
    else:
        accept = False
    # Alternative method
    # if "democheckbox" in request.form:
    #     accept = True
    # else:
    #     accept = False
            # Force the user to check the checkbox
            # return render_template("form.template.html", message = "Please tick check box", context=context)
    # ***most eficient way to code***
    # accept = True if request.form.get("democheck") == "yes" else False

    return render_template('form.template.html',
                            name = name,
                            sex = sex,
                            comment = comment,
                            contact = contact,
                            accept = accept
    )
    
    # Make the results into a dictionary
    # return render_template('form.template.html', context = {
        # "name": name,
        # "sex": sex,
        # "comment": comment,
        # "contact": contact,
        # "accept": accept
    # })

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
