import os
import json
# import Flask class from flask module
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# create instance of the the class and store in a variable
app = Flask(__name__)
app.secret.key = os.environ.get("SECRET_KEY")

# thanks to the decorator when we browse to root directory flask tiggers index function
# this function is called view
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # first member is variable passed to html, second is the member object
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your messahe".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

# main is the name of inbuilt module in Python, but we don't import it
# we use os module to get IP environ variable if it exists
# 5000 is a common port used by Flask
# debug should only be set to True during development, never in production/when sending for assessment


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )