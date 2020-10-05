from flask_mongoalchemy import MongoAlchemy

# create a MongoAlchemy object
db = MongoAlchemy()


def intialize_db_config(app):

    # MONGOALCHEMY_SERVER='localhost',
    app.config["MONGOALCHEMY_USER"] = 'root'
    app.config["MONGOALCHEMY_PASSWORD"] = 'example'
    app.config["MONGOALCHEMY_DATABASE"] = 'flaskdo'
    app.config["MONGOALCHEMY_SERVER_AUTH"] = True

    # database connection configurations
    db.init_app(app)
