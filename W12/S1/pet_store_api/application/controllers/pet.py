import flask
from flask import request, redirect, flash, render_template, url_for
# from application.extensions.database import db
# from application.models import Todo

pet_bp = flask.Blueprint(
    'pet',
    __name__,
    template_folder='../templates'
)


@todo_bp.route('/', methods=['GET', 'POST'])
def index():
    todo = Todo.query.order_by('-id')
    _form = request.form

    if request.method == 'POST':
        title = _form["title"]
        td = Todo(title=title)
        try:
            td.store_to_db()
            flash("add task successfully!")
            return redirect(url_for('todo.index'))
        except Exception as e:
            print(e)
            flash("fail to add task!")

    return render_template('index.html', todo=todo)
