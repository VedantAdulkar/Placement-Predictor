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
    ssc_marks = float(request.form.get("ssc"))
    hsc_marks = float(request.form.get("hsc"))
    cgpa = float(request.form.get("cgpa"))
    project_count = int(request.form.get("project_count"))
    SoftSkillsRating = float(request.form.get("SoftSkillsRating"))
    internship_count = int(request.form.get("internship_count"))
    aptitude_score = float(request.form.get("aptitude_score"))
    workshop_attended = int(request.form.get("workshop_attended"))
    e_activities = int(request.form.get("EActivities"))
    p_training = int(request.form.get("PTraining"))

    # Example of processing the input values (modify as needed)
    input_values = [ssc_marks, hsc_marks, cgpa, project_count, internship_count, SoftSkillsRating, aptitude_score, workshop_attended, e_activities, p_training]


    # Convert input values to floating-point numbers if needed
    float_features = [float(x) for x in input_values]  # Modify this line based on your input data type

    # Make prediction using the model
    features = [np.array(float_features)]
    #prediction = model.predict(features)

    # Render the HTML template and pass the input values and prediction result , prediction_text="Your Placement Possibility is {}".format(prediction)
    return render_template("index.html", input_values=input_values)

if __name__ == "__main__":
    flask_app.run(debug=True)