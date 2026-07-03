<h1 align="center">🚖 NYC Taxi Trip Duration Prediction</h1>

<p align="center">
Machine Learning • FastAPI • Docker • Render • Scikit-Learn
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.13-blue">
<img src="https://img.shields.io/badge/Scikit--Learn-ML-orange">
<img src="https://img.shields.io/badge/FastAPI-API-green">
<img src="https://img.shields.io/badge/Docker-Container-blue">
<img src="https://img.shields.io/badge/Render-Deployed-success">
<img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

# 🌐 Live Demo

🚀 **Live API**

https://nyc-taxi-trip-duration-api.onrender.com/

📄 **Swagger Documentation**

https://nyc-taxi-trip-duration-api.onrender.com/docs

---

# 📌 Project Overview

This project predicts the duration of New York City taxi trips using Machine Learning.

It covers the complete Machine Learning lifecycle, from preprocessing and feature engineering to deployment as a production-ready REST API.

The application is containerized using Docker and deployed on Render, allowing users to make real-time predictions through FastAPI.

---

# ✨ Highlights

- 🚖 Predicts NYC Taxi Trip Duration
- 📊 Trained on **1.45 Million+ Trips**
- ⚡ Achieved **R² Score: 0.7674**
- 🧹 Complete Data Cleaning Pipeline
- 📈 Feature Engineering
- 🤖 Random Forest Regression
- 🚀 FastAPI REST API
- 🐳 Dockerized
- ☁️ Deployed on Render

---

# 🏗️ Project Architecture

```text
                NYC Taxi Dataset
                       │
                       ▼
              Data Cleaning
                       │
                       ▼
            Feature Engineering
                       │
                       ▼
          Random Forest Regressor
                       │
                       ▼
               Saved Model (.pkl)
                       │
                       ▼
                  FastAPI API
                       │
                       ▼
                  Docker Image
                       │
                       ▼
               Render Deployment
                       │
                       ▼
              Public REST API
```

---

# 📊 Dataset

Dataset: **NYC Taxi Trip Duration**

### Target Variable

- Trip Duration

### Features Used

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

# 🛠 Data Preprocessing

Performed the following preprocessing steps:

- Removed duplicate records
- Removed missing values
- Removed unrealistic trips
- Removed abnormal trip durations
- Removed extremely slow trips
- Removed long-distance outliers
- One-Hot Encoding
- Log Transformation of Target Variable

---

# ⚙️ Feature Engineering

Implemented Features

- Pickup Hour
- Pickup Day
- Pickup Month
- Pickup Weekday
- Weekend Indicator
- Peak Hour Indicator
- Time of Day Classification
- Haversine Distance Calculation

---

# 🤖 Machine Learning Model

### Algorithm

- Random Forest Regressor

### Libraries Used

- Pandas
- NumPy
- Scikit-Learn
- FastAPI
- Joblib

---

# 📈 Model Performance

| Metric | Value |
|---------|-------|
| MAE | **191.11 sec** |
| RMSE | **318.94 sec** |
| R² Score | **0.7674** |

---

# 📊 Feature Importance

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Distance | 82.75% |
| 2 | Pickup Hour | 5.00% |
| 3 | Dropoff Latitude | 3.98% |
| 4 | Dropoff Longitude | 1.83% |
| 5 | Pickup Longitude | 1.70% |

---

# 🚀 REST API

## Home

```
GET /
```

Returns

```json
{
  "message":"Welcome to Taxi Trip Duration Prediction API"
}
```

---

## Prediction

```
POST /predict
```

Example Request

```json
{
  "pickup_longitude": -73.985428,
  "pickup_latitude": 40.748817,
  "dropoff_longitude": -73.985001,
  "dropoff_latitude": 40.758896,
  "pickup_hour": 18,
  "pickup_day": 15,
  "pickup_month": 6,
  "pickup_weekday": 2,
  "is_weekend": 0,
  "distance": 1.15,
  "is_peak_hour": 1,
  "time_of_day_Morning": 0,
  "time_of_day_Night": 0
}
```

Example Response

```json
{
  "predicted_trip_duration_seconds": 619.13,
  "predicted_trip_duration_minutes": 10.32
}
```

---

# 📸 Project Screenshots

## 📁 Project Structure

![Project Structure](screenshots/project-structure.png)

---

## 🚀 Swagger UI

![Swagger](screenshots/swagger-ui.png)

---

## 🔮 Prediction Response

![Prediction](screenshots/prediction-response.png)

---

## 📈 Model Performance

![Performance](screenshots/model-performance.png)

---

## 🔥 Correlation Heatmap

![Heatmap](screenshots/correlation-heatmap.png)

---

## 📉 Trip Duration Distribution

![Distribution](screenshots/trip-duration-distribution.png)

---

## 🚖 Distance vs Trip Duration

![Scatter](screenshots/distance-vs-trip-duration.png)

---

# 📂 Project Structure

```text
NYC-Taxi-Trip-Duration-Prediction
│
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── feature_columns.pkl
├── taxi_trip_duration_model.pkl
├── README.md
├── .gitignore
│
├── notebook/
│   └── NYC_Taxi_Trip_Duration_Prediction.ipynb
│
└── screenshots/
    ├── banner.png
    ├── project-structure.png
    ├── swagger-ui.png
    ├── prediction-response.png
    ├── feature-importance.png
    ├── model-performance.png
    ├── correlation-heatmap.png
    ├── trip-duration-distribution.png
    └── distance-vs-trip-duration.png
```

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- FastAPI
- Docker
- Joblib
- Git
- GitHub
- Render

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/Adityasinghrajput01/NYC-Taxi-Trip-Duration-Prediction.git
```

Move into the project

```bash
cd NYC-Taxi-Trip-Duration-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

Build the Docker image

```bash
docker build -t nyc-taxi-api .
```

Run the container

```bash
docker run -p 8000:8000 nyc-taxi-api
```

---

# ☁️ Deployment

The application is deployed on **Render** using **Docker**.

🌐 Live URL

https://nyc-taxi-trip-duration-api.onrender.com/

📄 Swagger

https://nyc-taxi-trip-duration-api.onrender.com/docs

---

# 🎯 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Outlier Detection
- Random Forest Regression
- Model Evaluation
- FastAPI
- REST API Development
- Docker
- Git
- GitHub
- Cloud Deployment

---

# 🔮 Future Improvements

- Hyperparameter Tuning
- XGBoost & LightGBM
- Model Monitoring
- CI/CD Pipeline
- Automated Retraining
- Frontend Dashboard
- Authentication & Rate Limiting

---

# 👨‍💻 Author

## Aditya Kumar Singh

**GitHub**

https://github.com/Adityasinghrajput01

**LinkedIn**

https://www.linkedin.com/in/aditya-kumar-singh-173911321/

---

<p align="center">

⭐ If you found this project useful, please consider giving it a Star!

Made with ❤️ by <b>Aditya Kumar Singh</b>

</p>
