from flask_restful import Resource, Api


class Pet(Resource):
    def get(self):
        return {'hello': 'world'}
