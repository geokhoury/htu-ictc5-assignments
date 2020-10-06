from flask import Flask, render_template, request, jsonify
from wtforms import IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import requests
import json


class AddForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])


DEBUG = True
SECRET_KEY = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/test/x")
def test_x():
    r = requests.get('http://localhost:8080/api/v1/path_for_blueprint_x/test')

    return r.json()


@app.route("/test/y")
def test_y():
    r = requests.get('http://localhost:8080/api/v1/path_for_blueprint_y/test')

    return r.json()


@app.route("/tasklists")
def tasklists():
    # Build JSON for API request
    data = {"user_id": "5f7af9b4f8f780280e44c0b2"}

    # Retrieve the user tasklists
    r = requests.post(
        'http://localhost:8080/api/v1/user/tasklists', json=data)

    # Render the tasklists view with the tasklists
    return render_template("tasklists.html", tasklists=r.json())


@app.route("/tasklist/<tasklist_id>")
def view_tasklist(tasklist_id):
    # Retrieve task list data
    r = requests.get(
        'http://localhost:8080/api/v1/tasklist/' + tasklist_id)

    tasklist = json.loads(r.json())
    print(tasklist['tasks'])
    return render_template("tasklist.html", tasklist=tasklist)


if __name__ == "__main__":
    app.run()
