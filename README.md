# ML Portfolio Dashboard: Placement Predictor

A state-of-the-art Machine Learning web application built with Flask that predicts a student's placement probability based on various academic and extracurricular features. It features a modern dark-mode SaaS UI designed to showcase Data Science skills and model insights.

## Features

- **Predictive Model**: Uses a Random Forest Classifier to predict the precise probability of placement.
- **Model Insights**: Features an interactive Chart.js visualization on the dashboard that exposes the model's inner workings by plotting **Feature Importances**.
- **Interactive UI**: A sleek, responsive, two-column CSS grid dashboard with real-time probability gauges.
- **Input Parameters**: Considers 10 distinct features including:
  - CGPA, SSC & HSC marks
  - Internships & Project Count
  - Workshops Attended & Aptitude Score
  - Soft Skills Rating, Extracurriculars, & Placement Training

## Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML5, CSS3 Variables & Flexbox/Grid, Chart.js, Google Fonts (Outfit & Inter)

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Placement-Predictor
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model** (Optional, if `model.pkl` is not present):
   ```bash
   python model.py
   ```
   This will train the Random Forest model on the dataset (`placedata.csv`) and save it as `model.pkl`.

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

5. **Access the Dashboard**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.