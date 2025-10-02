from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model, scaler = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(feature)) for feature in
                    ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                     'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
        final_features = scaler.transform([features])
        prediction = model.predict(final_features)[0]
        prediction_proba = model.predict_proba(final_features)[0][1]

        result = "Diabetic" if prediction == 1 else "Non-Diabetic"
        confidence = f"{prediction_proba*100:.2f}% confidence"

        return render_template('index.html',
                               prediction_text=f"Prediction: {result}",
                               confidence_text=f"Confidence: {confidence}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
