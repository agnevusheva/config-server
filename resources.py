from flask_restful import Resource

class DataResource(Resource):
    def get(self):
        return {'data': 'Hello, World!'}

from resources import DataResource

api.add_resource(DataResource, '/data')