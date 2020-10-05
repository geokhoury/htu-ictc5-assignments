from flask import Flask, render_template, request
from wtforms import IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import requests
import json


class AddForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])


class DivideForm(FlaskForm):
    x = IntegerField('X', validators=[DataRequired()])
    y = IntegerField('Y', validators=[DataRequired()])


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


@app.route("/test/add/<int:number>")
def test_add(number):
    # Build JSON payload to send to API
    data = {'number': number}

    # Post the data to the API
    r = requests.post(
        'http://localhost:8080/api/v1/path_for_blueprint_x/add', json=data)

    print(f"Response status code: {r.status_code}.")

    # Return the JSON response from the API
    return r.json()


@app.route("/test/subtract/<int:number>")
def test_subtract(number):
    # Build JSON payload to send to API
    data = {'number': number}

    # Post the data to the API
    r = requests.post(
        'http://localhost:8080/api/v1/path_for_blueprint_y/subtract', json=data)

    # Return the JSON response from the API
    return r.json()


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        # Build JSON payload to send to API
        data = {'number': form.number.data}

        # Post the data to the API
        r = requests.post(
            'http://localhost:8080/api/v1/path_for_blueprint_x/add', json=data)

        # Render the result template with the msg from the API
        return render_template("result.html", msg=r.json()['msg'])

    # Render the add template with the add form
    return render_template("add.html", form=form)


@app.route("/divide", methods=["GET", "POST"])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        # Build JSON payload to send to API
        data = {
            'x': form.x.data,
            'y': form.y.data
        }

        # Post the data to the API
        r = requests.post(
            'http://localhost:8080/api/v1/path_for_blueprint_y/divide', json=data)

        # Render the result template with the msg from the API
        return render_template("result.html", msg=r.json()['msg'])

    # Render the add template with the add form
    return render_template("divide.html", form=form)


if __name__ == "__main__":
    app.run()
