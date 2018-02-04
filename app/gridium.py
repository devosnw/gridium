import flask
import requests

API_URL = ('https://snapmeter.com/api/v2/531e19848df5cb0b35014e85/meters'
           '/2166484536790/bill-summary?token=6d547442-417b-41a3-8838-'
           'b022f9c2974d')
app = flask.Flask(__name__)


def get_bills():
    return requests.get(API_URL).json()


@app.route('/')
def home():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
