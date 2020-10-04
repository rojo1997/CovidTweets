from flask_restful import Resource, reqparse
import numpy as np

class OnDemand(Resource):
    def __init__(self, estimator):
        self.estimator = estimator
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('tweets')

    def get(self):
        args = self.parser.parse_args()
        pred = self.estimator.predict(np.array([args['tweets']]))
        return({
            'pred': pred
        })