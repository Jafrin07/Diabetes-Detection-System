# Diabetes-Detection-System

A web-based application built using Flask that predicts the likelihood of diabetes based on user input. It leverages a machine learning model trained on health data and provides a clean, interactive interface for users to receive predictions.

## Project Structure

Diabetes Detection System/
├── app/                  # Flask application logic
│   └── routes.py         # Main route handling
├── static/               # CSS, JS, and image assets
├── templates/            # HTML templates
├── diabetes_model.pkl    # Pre-trained ML model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

## Features

- Predicts diabetes risk using a trained ML model
- User-friendly web interface built with Flask
- Clean UI with Bootstrap or custom CSS
- Modular and scalable codebase

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/diabetes-detection-system.git
cd diabetes-detection-system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app/routes.py
```

Then open your browser and go to:  
`http://127.0.0.1:5000`

---

## Model Overview

The model was trained using a dataset with the following features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

It outputs a binary prediction:  
**Diabetic** or **Not Diabetic**

Final training metrics:
- Accuracy: 83.9%
- Validation Accuracy: 80.5%
- Loss: 0.3466
- Validation Loss: 0.4593

## Requirements

- Python 3.7+
- Flask
- scikit-learn
- pandas
- numpy

(See `requirements.txt` for full list)

---

## Deployment

You can deploy this app using platforms like:
- [Render](https://render.com)
- [Heroku](https://heroku.com)
- [Vercel](https://vercel.com) (with Flask adapter)

Let me know if you want help setting up deployment.

---

## License

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute.


Let me know if you'd like to include instructions for training the model, uploading it to GitHub, or adding badges and screenshots. I can help you polish it even further.
