from flask import Flask, request
import json
import os

input = {
    "charecter": "[str]",
    "scenario": "[str]",
    "challange": "[str]"
}

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Checks if the API works"""
    return 'Alive!'


@app.route("/bubble", methods=["GET"])
def input_format():

    return input


@app.route("/bubble", methods=["POST"])
def respond():
    """This function gets the user input in Json format"""

    data = request.get_json()
    charecter = data['charecter']
    scenario = data['scenario']
    challange = data['challange']

    return data['charecter']


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", threaded=True, port=port)

