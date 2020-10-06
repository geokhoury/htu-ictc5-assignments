from flask import Blueprint, jsonify, request
from datetime import datetime
from ..models import User, TaskList
from mongoengine import *

# define the blueprint
user_blueprint = Blueprint(name="user_blueprint", import_name=__name__)

# add create user function to the blueprint


@user_blueprint.route('/create', methods=['POST'])
def create_user():
    # Read the request data from the client
    data = request.get_json()

    # Create and save a user to the DB
    user = User(username=data['username'],
                password=User.generate_hash(data['password']),
                first_name=data['first_name'],
                last_name=data['last_name'],
                created_at=datetime.now()
                ).save()

    return user.to_json()


@user_blueprint.route('/login', methods=['POST'])
def login():
    # Read the request data from the client
    data = request.get_json()

    # Read credentials from request
    username = data['username']
    password = data['password']

    # Authenticate the user
    if User.authenticate(username, password):
        # Add user to session
        session['user'] = user.to_json()
        response = {"msg": f"User {username} is now logged in."}
        return jsonify(response)
    else:
        response = {"msg": "Invalid credentials."}
        return jsonify(response)

# add user tasklists function to the blueprint


@user_blueprint.route('/tasklists', methods=['POST'])
def user_tasklists():
    data = request.get_json()

    # Retrieve the tasklist
    tasklists = TaskList.objects(owner_id=data['user_id']).all()

    return tasklists.to_json()
