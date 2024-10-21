from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/submit", methods = ["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/get", methods = ["GET"])
def process_query(query):
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
