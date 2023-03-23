import os
# import Flask class from flask module
from flask import Flask, render_template

# create instance of the the class and store in a variable
app = Flask(__name__)

# thanks to the decorator when we browse to root directory flask tiggers index function
# this function is called view
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

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