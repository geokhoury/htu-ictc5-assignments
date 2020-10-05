from flask import Blueprint, jsonify, request

# define the blueprint
blueprint_y = Blueprint(name="blueprint_y", import_name=__name__)

# note: global variables can be accessed from view functions
y = 5

# add view function to the blueprint


@blueprint_y.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_y."}
    return jsonify(output)

# add view function to the blueprint


@blueprint_y.route('/subtract', methods=['POST'])
def subtract_y():
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and output as JSON
    result = in_val - y
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)


@blueprint_y.route('/divide', methods=['POST'])
def divide_xy():
    # retrieve body data from input JSON
    data = request.get_json()
    x_val = data['x']
    y_val = data['y']

    # compute result and output as JSON
    output = {}

    if y_val == 0:
        output = {"msg": f"You cannot divide by zero."}
    else:
        result = x_val / y_val
        output = {
            "msg": f"Your result is: '{result}'",
            "result": result
        }

    # return the JSON output
    return jsonify(output)
