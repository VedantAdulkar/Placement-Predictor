import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route('/static')
def send_static(path):
    return send_from_directory('static', path)

@flask_app.route("/predict", methods=["POST"])
def predict():
    # Get the input values from the form
    input_values = request.form.values()

    # Convert input values to a list
    input_list = list(input_values)

    # Convert input values to floating-point numbers if needed
    float_features = [float(x) for x in input_list]  # Modify this line based on your input data type

    # Make prediction using the model
    features = [np.array(float_features)]
    prediction = model.predict(features)

    # Render the HTML template and pass the input values and prediction result
    return render_template("index.html", input_values=input_list, prediction_text="Your Placement Possibility is {}".format(prediction))


#@flask_app.route("/predict", methods = ["POST"])
#def predict():
#    input_values = request.form.values()
#    float_features = [float(x) for x in request.form.values()]
#    features = [np.array(float_features)]
#    prediction = model.predict(features)
#    return render_template("index.html", input_values=input_values, prediction_text = "Your Placement Possibility is {}".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)