from flask import Flask, request, Blueprint, render_template, redirect, session, url_for, jsonify
from ..models import TaskList, Task, User
from ..core import login_required
from bson.objectid import ObjectId

# create a blueprint
bp = Blueprint('tasklists', __name__)


@bp.route('/tasklist/create', methods=['GET', 'POST'])
@login_required
def create_tasklist():
    if request.method == 'GET':
        # render the create tasklist template
        return render_template('tasklist/create.html')
    else:
        # read values from the form submit
        name = request.form['list-name']
        description = request.form['list-description']

        # create a tasklist document
        tasklist = TaskList(name=name, description=description,
                            owner_id=session['user']['id'])

        # save the tasklist document
        tasklist.save()

        # get the logged in user
        user = User.query.get_or_404(session['user']['id'])

        # add the newly created tasklist
        user.add_tasklist(str(tasklist.mongo_id))

        # save the changes to the user object
        user.save()

        # update the session
        session['user'] = user.serialized

        # redirect to the index
        return redirect(url_for('tasklists.tasklists'))


@bp.route('/tasklist/<string:tasklist_id>')
@login_required
def view_tasklist(tasklist_id):
    tasklist = TaskList.query.get_or_404(tasklist_id)
    tasks = Task.query.filter(Task.tasklist_id == tasklist_id).all()
    return render_template('tasklist/view.html', tasklist=tasklist, tasks=tasks)


@bp.route('/tasklist/update/<string:tasklist_id>')
@login_required
def update_tasklist(tasklist_id):
    pass


@bp.route('/tasklist/delete/<string:tasklist_id>')
@login_required
def delete_tasklist(tasklist_id):
    # retrieve the tasklist
    tasklist = TaskList.query.get_or_404(tasklist_id)

    # delete the tasklist
    tasklist.remove()

    # redirect the user to the tasklists
    return redirect(url_for('tasklists.tasklists'))


@bp.route('/tasklists')
@login_required
def tasklists():
    # create a list to store the tasklists
    tasklists = TaskList.query.filter(
        TaskList.owner_id == session['user']['id'])

    # render the task lists template
    return render_template('tasklist/task-lists.html', tasklists=tasklists)


@bp.route('/test')
def test():
    tasklists = TaskList.query.filter({"mongo_id": {"$in":
                                                    [ObjectId("5f68670ac60b9f25ad252b04"),
                                                     ObjectId(
                                                         "55bf528e69b70ae79be35006")
                                                     ]
                                                    }}).all()

    print(tasklists)
    return redirect("/")
    # return jsonify(tasklists)

# @bp.route('/user/update/<int:user_id>', methods=['POST'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     form = UserForm()
#     if form.validate_on_submit():
#         form.instance = user
#         form.save()
#         return redirect(url_for('list_user'))
#     form = UserForm(document=user)
#     return render_template('/user/edit.html', form=form, user=user)
