from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))  # Load model 

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/result", methods=["POST"])
def result():
    # Get the input values from the form
    input_values = [request.form.get(field) for field in ["cgpa", "internship_count", "project_count", "workshop_attended", "aptitude_score", "SoftSkillsRating", "EActivities", "PTraining", "ssc", "hsc"]]
    input_array = np.array(input_values)
    prediction = model.predict(input_array.reshape(1, -1))

    if prediction == 1:
        prediction_text = "You will get Placed..!!"
        prediction_image = "/static/place2.png"
    else:
        prediction_text = "You won't get Placed..!!"
        prediction_image = "/static/nplace2.png"   

    # Render the result page with input values as labels 
    return render_template("result.html", input_values=input_values, prediction_text = prediction_text, prediction_image = prediction_image)

@flask_app.route("/clear", methods=["GET"])
def clear():
    # Redirect to the home page with cleared input fields
    return redirect(url_for("home"))

if __name__ == "__main__":
    flask_app.run(debug=True)
