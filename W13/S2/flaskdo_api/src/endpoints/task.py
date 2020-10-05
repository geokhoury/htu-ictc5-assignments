from flask import Blueprint, jsonify, request

# define the blueprint
task_blueprint = Blueprint(name="task_blueprint", import_name=__name__)

# note: global variables can be accessed from view functions
y = 5

# add view function to the blueprint


@task_blueprint.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_y."}
    return jsonify(output)

# add view function to the blueprint


@task_blueprint.route('/subtract', methods=['POST'])
def subtract_y():
    # retrieve body data from input JSON
    data = request.get_json()
    in_val = data['number']
    # compute result and output as JSON
    result = in_val - y
    output = {"msg": f"Your result is: '{result}'"}
    return jsonify(output)
