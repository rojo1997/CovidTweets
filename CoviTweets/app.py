
from flask import Flask
from flask_restful import Resource, Api, reqparse
from dill import load, dump
import sys
import os

from CovidTweets.api import OnDemand

app = Flask(__name__)
api = Api(app)

estimator = load(file = open('../models/model.plk', mode = 'rb'))

api.add_resource(
    OnDemand, 
    '/ondemand/',
    resource_class_kwargs = {
        'estimator': estimator
    }
)

if __name__ == '__main__':
    params = {
        'host': "0.0.0.0",
        'debug': True,
        'port': 5000
    }
    if os.environ.get('COVID_TWEETS_DEBUG') != None:
        params['debug'] = os.environ['COVID_TWEETS_DEBUG']
    if os.environ.get('COVID_TWEETS_PORT') != None:
        params['port'] = int(os.environ['COVID_TWEETS_PORT'])
    app.run(**params)