from flask import Blueprint, jsonify, request
from datetime import datetime
from ..models import TaskList, Task
from mongoengine import *
import json

# define the blueprint
tasklist_blueprint = Blueprint(name="tasklist_blueprint", import_name=__name__)

# note: global variables can be accessed from view functions
x = 5

# add view function to the blueprint


@tasklist_blueprint.route('/test', methods=['GET'])
def test():
    output = {
        "msg": "I'm the test endpoint from the tasklist blueprint."
    }
    return jsonify(output)

# add view tasklist function to the blueprint


@tasklist_blueprint.route('/<tasklist_id>', methods=['GET'])
def view_tasklist(tasklist_id):

    # Retrieve the tasklist
    tasklist = TaskList.objects(id=tasklist_id).first()

    # Find all tasks for this tasklist
    tasks = Task.objects(tasklists__in=[tasklist]).all()

    # Load JSON from DB into JSON object
    json_tasklist = json.loads(tasklist.to_json())
    json_tasks = {"tasks": json.loads(tasks.to_json())}

    # Append tasks to tasklist
    json_tasklist.update(json_tasks)

    # Return JSON response
    return jsonify(json.dumps(json_tasklist))

# add create tasklist function to the blueprint


@ tasklist_blueprint.route('/create', methods=['POST'])
def create_tasklist():
    # Read JSON data from request from the client
    data = request.get_json()

    # Create and save a new task list
    tasklist = TaskList(
        name=data['name'],
        description=data['description'],
        owner_id=data['user_id'],
        created_at=datetime.now()
    ).save()

    # Create test tasks
    task = Task(title="Demo task 1", description="First task on this list!",
                created_at=datetime.now(), tasklists=[tasklist]).save()
    task = Task(title="Demo task 2", description="Second task on this list!",
                created_at=datetime.now(), tasklists=[tasklist]).save()
    return tasklist.to_json()

# add delete tasklist function to the blueprint


@ tasklist_blueprint.route('/<tasklist_id>', methods=['delete'])
def delete_tasklist(tasklist_id):

    # Retrieve the tasklist
    tasklist = TaskList.objects(id=tasklist_id).first()

    if tasklist is not None:
        tasklist.delete()
        return jsonify({"msg": f"Task list {tasklist_id} has been deleted."})
    else:
        return jsonify({"msg": f"Task list {tasklist_id} does not exist."})

# add view tasklists function to the blueprint


@ tasklist_blueprint.route('/all')
def view_tasklists():

    # Retrieve the tasklist
    tasklist = TaskList.objects()

    # Find all pages Bob authored
    tasklist.tasks = Task.objects(authors__in=[tasklist])

    return tasklist.to_json()
