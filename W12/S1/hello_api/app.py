import json
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class User(Resource):
    our_user = {
        'id': 1,
        'first_name': 'Cookie',
        'last_name': 'Monster',
        'age': 22
    }

    def get(self):
        return jsonify(self.our_user)


api.add_resource(HelloWorld, '/')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
