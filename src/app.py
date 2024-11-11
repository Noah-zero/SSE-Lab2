from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/submitGithubUsername", methods=["POST"])
def submitGithubUsername():
    input_name = request.form.get("githubUsername")
    return render_template("hello.html", name=input_name)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/query", methods=["GET"])
q = request.args.get("query")
if q == "dinosaurs":
    return "Dinosaurs ruled the Earth 200 million years ago"
else:
    return "Unknown"
