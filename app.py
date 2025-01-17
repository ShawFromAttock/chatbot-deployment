from flask import Flask, render_template, request, redirect, jsonify
from chat import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "main":
    app.run(debug=True)
