import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)
model_clone = joblib.load('model.pkl')

@app.route("/")
def hello_world():
    return f"<p>Hello</p>"

@app.route('/get-prediction')
def generate_a_prediction():
    time = request.args.get('time')
    risk = request.args.get('risk')
    
    result = { "result": int(model_clone.predict([[time, risk]])[0]) }
    return result

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()