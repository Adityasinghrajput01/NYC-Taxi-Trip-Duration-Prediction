# 🚖 NYC Taxi Trip Duration Prediction

A Machine Learning project that predicts the duration of NYC taxi trips using historical trip data. The project includes data preprocessing, feature engineering, model training, evaluation, and deployment using FastAPI.

---

## 📌 Project Overview

The objective of this project is to estimate the trip duration of a taxi ride based on pickup and dropoff locations and trip-related features.

The project follows the complete Machine Learning lifecycle:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- FastAPI Deployment

---

## 📊 Dataset

Dataset: NYC Taxi Trip Duration

Features used:

- Pickup Longitude
- Pickup Latitude
- Dropoff Longitude
- Dropoff Latitude
- Pickup Hour
- Pickup Day
- Pickup Month
- Pickup Weekday
- Distance
- Peak Hour
- Weekend Indicator
- Time of Day

---

## 🛠 Feature Engineering

Implemented:

- Pickup Hour
- Pickup Day
- Pickup Month
- Pickup Weekday
- Weekend Detection
- Peak Hour Detection
- Time of Day Classification
- Haversine Distance Calculation
- Log Transformation of Target Variable

---

## 🤖 Machine Learning Model

Algorithm:

- Random Forest Regressor

Libraries:

- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Joblib

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| MAE | 191.11 seconds |
| RMSE | 318.94 seconds |
| R² Score | 0.7674 |

---

## 🚀 API Deployment

FastAPI was used to deploy the trained model.

Available endpoints:

### GET /

Returns API status.

### GET /health

Returns server health.

### POST /predict

Predicts trip duration.

---

## 📂 Project Structure

```
NYC-Taxi-Trip-Duration-Prediction
│
├── app.py
├── requirements.txt
├── feature_columns.pkl
├── README.md
├── .gitignore
└── new york estimated ml time.ipynb
```

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- FastAPI
- Joblib
- Git
- GitHub

---

## 🔮 Future Improvements

- Docker Deployment
- Cloud Deployment (Render)
- Hyperparameter Tuning
- XGBoost Model
- CI/CD Pipeline
- Model Monitoring

---

## 👨‍💻 Author

Aditya Kumar Singh

GitHub:
https://github.com/Adityasinghrajput01
