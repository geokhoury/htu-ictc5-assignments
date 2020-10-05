from flask import Flask, request, Blueprint, render_template, redirect, session, url_for
from ..models.user import User
from ..models.task import Task

# create a blueprint
bp = Blueprint('user', __name__)


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # if HTTP method is GET
    if request.method == 'GET':
        # render the signup template
        return render_template('login/signup.html')

    # if HTTP method is POST
    else:
        # read values from the signup form submit
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        address = request.form['address']

        # create a user document
        user = User(first_name=first_name, last_name=last_name,
                    username=username, email=email, password=password, address=address, tasklists=[])

        # save the user document
        user.save()

        # render the login template
        return redirect('/login')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # if HTTP method is GET
    if request.method == 'GET':
        # render the login template
        return render_template('login/login.html')
    else:
        # read values from the login form
        username = request.form['username']
        password = request.form['password']

        # get User object based on the filter 'username'
        # User.username (DB) == username (form)
        user = User.query.filter(User.username == username).first()
        results = Task.query.filter(
            {
                '$or': [
                    {Task.title: {"$regex": search_keyword}},
                    {Task.description: {"$regex": search_keyword}}
                ]
            }
        ).all()

        print(len(results))
        print("Results: " + str(results))

        # check the authentication based on the password from the form
        if user.authenticate(password):
            # add the serialized user object into the session
            session['user'] = user.serialized
            session['my_special_variable'] = 42
            session['is_logged_in'] = True

            # render the index template
            return render_template('index.html')

        # redirect to /403
        return redirect('/403')


@ bp.route('/logout')
def logout():
    # clear the session 'user' attribute
    session.clear()

    # redirect to /
    return redirect(url_for('home.index'))


@ bp.route('/user/<int:user_id>')
def view_user(user_id):
    pass


@ bp.route('/user/delete/<int:user_id>')
def delete_user(user_id):
    pass


@ bp.route('/user/edit/<int:user_id>')
def edit_user(user_id):
    pass


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
