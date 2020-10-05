from flask import Blueprint, jsonify, request
from datetime import datetime

# define the blueprint
blueprint_x = Blueprint(name="blueprint_x", import_name=__name__)

# note: global variables can be accessed from view functions
x = 5

# add view function to the blueprint


@blueprint_x.route('/test', methods=['GET'])
def test():
    output = {
        "msg": "I'm the test endpoint from blueprint_x.",
        "another_msg": f"The value of global 'x' is {x}.",
        "timestamp": datetime.now()
    }
    return jsonify(output)

# add view function to the blueprint


@blueprint_x.route('/add', methods=['POST'])
def add_x():
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']

    # compute result and output as JSON
    result = in_val + x
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)


@blueprint_x.route('/multiply', methods=['POST'])
def multiply_xy():
    # retrieve body data from input JSON
    data = request.get_json()
    x_val = data['x']
    y_val = data['y']

    # compute result and output as JSON
    result = x_val * y_val
    output = {
        "msg": f"Your result is: '{result}'",
        "result": result
    }
    return jsonify(output)
