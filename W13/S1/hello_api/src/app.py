"""Flask Application"""

# load libaries
from flask import Flask, jsonify
import sys

# load modules
from src.endpoints.blueprint_x import blueprint_x
from src.endpoints.blueprint_y import blueprint_y

# init Flask app
app = Flask(__name__)

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_x, url_prefix="/api/v1/path_for_blueprint_x")
app.register_blueprint(blueprint_y, url_prefix="/api/v1/path_for_blueprint_y")

# app.register_blueprint(tasklist, url_prefix="/api/v1/tasklist")
# app.register_blueprint(task, url_prefix="/api/v1/task")
# app.register_blueprint(user, url_prefix="/api/v1/user")
