# Diabetes Prediction Model API

This is a FastAPI-based application that predicts whether a person is diabetic based on several health parameters using a pre-trained machine learning model.

## Features

- **Prediction Endpoint**: Accepts multiple health-related parameters via query parameters and returns a prediction (`diabetic` or `not diabetic`).
- The model is pre-trained and saved using `scikit-learn`.

## How It Works

The API uses a machine learning model trained to predict whether a person is diabetic or not based on the following input parameters:

- `pregnancies` (int): Number of pregnancies
- `Glucose` (int): Glucose level
- `BloodPressure` (int): Blood pressure level
- `SkinThickness` (int): Skin thickness in mm
- `Insulin` (int): Insulin level
- `BMI` (float): Body Mass Index
- `DiabetesPedigreeFunction` (float): Diabetes Pedigree Function
- `Age` (int): Age of the person

The API responds with a JSON object that contains the result:
```json
{
  "result": "The person is diabetic"  // or "The person is not diabetic"
}
```

## API Endpoint

**GET** `/api/diabetes_prediction`

### Example Request

```bash
curl -X 'GET' \
  'https://diabetes-prediction-model-5d9550a8d37f.herokuapp.com/api/diabetes_prediction?pregnancies=2&Glucose=120&BloodPressure=80&SkinThickness=20&Insulin=85&BMI=25.5&DiabetesPedigreeFunction=0.5&Age=33' \
  -H 'accept: application/json'
```

### Example Response

```json
{
  "result": "The person is not diabetic"
}
```

## Requirements

The project uses the following dependencies:

- FastAPI
- Uvicorn
- scikit-learn
- Pydantic
- Requests

Make sure to install the dependencies listed in `requirements.txt` before running the project locally.
