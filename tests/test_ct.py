import unittest
import requests

class CovidTweetsTest(unittest.TestCase):
    def test1(self):
        session = requests.Session()
        h = session.get(
            url = 'http://localhost:5000/ondemand/',
            params = {
                'tweets': "Hola que tal"
            }
        )
        print(h)

    def test2(self):
        pass