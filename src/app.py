from flask import Flask, render_template, request
import requests as re


app = Flask(__name__)


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/query", methods=["GET"])
def query():
    query = request.args.get("q")
    if query == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"


@app.route("/submitgetgithubusername", methods=["POST"])
def submitgetgithubusername():
    data = []
    input_name = request.form.get("name")
    base_url = "https://api.github.com/users"
    user_repos_url = f"{base_url}/{input_name}/repos"
    response = re.get(user_repos_url)
    url = "https://api.github.com/repos/{}/{}/commits"
    if response.status_code == 200:
        for repo in response.json():
            temp = {}
            temp["name"] = repo['name']
            response1 = re.get(url.format(input_name,repo['name']))
            if response1.status_code == 200:
                try:
                    commit = response1.json()[0]
                    temp['SHA'] = commit['sha']
                    temp['Author'] = commit['commit']['author']['name']
                    temp['Date'] = commit['commit']['author']['date']
                    temp['Message'] = commit['commit']['message']
                except Exception:
                    continue
                data.append(temp)
    return render_template("github_username.html", name=input_name, data=data)


@app.route("/get_github_username", methods=["GET"])
def get_github_username():
    return render_template("get_github_username.html")


@app.route("/get_currency_exchange", methods=["GET", "POST"])
def get_currency_exchange():
    data = {}
    target = ["date","rates"]
    token = "f4f934d860f2881959b0bd1b9ff5efd4"
    url = "http://data.fixer.io/api/latest?access_key={}"
    response = re.get(url.format(token))
    if response.status_code == 200:
        data = {k: response.json()[k] for k in target if k in response.json()}
    return render_template("get_currency_exchange.html", data=data)