"""Flask Application"""

# load libaries
from flask import Flask, jsonify
from mongoengine import connect
import sys

# load modules
from src.endpoints.tasklist import tasklist_blueprint
from src.endpoints.task import task_blueprint
from src.endpoints.user import user_blueprint
from src.models import *

# init Flask app
app = Flask(__name__)

# connect to the DB
connect('flaskdo', host='localhost', port=27017, username='root',
        password='example', authentication_source='admin')

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(tasklist_blueprint, url_prefix="/api/v1/tasklist")
app.register_blueprint(task_blueprint, url_prefix="/api/v1/task")
app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")

# app.register_blueprint(tasklist, url_prefix="/api/v1/tasklist")
# app.register_blueprint(task, url_prefix="/api/v1/task")
# app.register_blueprint(user, url_prefix="/api/v1/user")
