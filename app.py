from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))  # Load model 

@flask_app.route("/")
def home():
    # Extract feature importances to showcase ML model insights
    importances = model.feature_importances_.tolist()
    feature_names = ["CGPA", "Internships", "Projects", "Workshops", "Aptitude Score", "Soft Skills", "Extracurriculars", "Placement Training", "SSC Marks", "HSC Marks"]
    
    return render_template("index.html", importances=importances, feature_names=feature_names)

@flask_app.route("/result", methods=["POST"])
def result():
    # Get the input values from the form, casting them safely to floats
    input_values = []
    for field in ["cgpa", "internship_count", "project_count", "workshop_attended", "aptitude_score", "SoftSkillsRating", "EActivities", "PTraining", "ssc", "hsc"]:
        val = request.form.get(field)
        # If value is empty or None, default to 0 to prevent crashes
        input_values.append(float(val) if val else 0.0)
        
    input_array = np.array(input_values)
    
    # Get probability of placement (class 1)
    probabilities = model.predict_proba(input_array.reshape(1, -1))[0]
    placement_prob = probabilities[1]
    
    # Format as a percentage string
    prob_percentage = round(placement_prob * 100, 1)

    # Determine message based on threshold
    if placement_prob >= 0.5:
        prediction_text = "Strong Profile"
        status_color = "#10b981" # Emerald green
    else:
        prediction_text = "Needs Improvement"
        status_color = "#f43f5e" # Rose red

    # Render the result page with input values and probability
    return render_template("result.html", 
                           input_values=input_values, 
                           prob_percentage=prob_percentage,
                           prediction_text=prediction_text,
                           status_color=status_color)



import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)
