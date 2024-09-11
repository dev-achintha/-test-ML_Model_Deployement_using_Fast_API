# Diabetes Prediction Model API

This is a FastAPI-based application that predicts whether a person is diabetic based on several health parameters using a pre-trained machine learning model.

## Features

- **Prediction Endpoint**: Accepts multiple health-related parameters via query parameters and returns a prediction (`diabetic` or `not diabetic`).
- The model is pre-trained and saved using `scikit-learn`.

## How It Works

The API uses a machine learning model trained to predict whether a person is diabetic or not based on the following input parameters:

- `pregnancies` (int): Number of pregnancies
- `Glucose` (int): Glucose level
- `BloodPressure` (int): Blood pressure level (mm Hg)
- `SkinThickness` (int): Triceps skin fold thickness (mm)
- `Insulin` (int): 2-Hour serum insulin (mu U/ml)
- `BMI` (float): Body Mass Index (weight in kg / (height in m²))
- `DiabetesPedigreeFunction` (float): Diabetes pedigree function
- `Age` (int): Age of the person

The API responds with a JSON object that contains the result:
```json
{
  "result": "The person is diabetic"  // or "The person is not diabetic"
}
```

## API Endpoint

### **GET** `/api/diabetes_prediction`

You can make requests to the following URL:

```
https://diabetes-prediction-model-5d9550a8d37f.herokuapp.com/docs

```

### Required Query Parameters:
- `pregnancies`: Integer
- `Glucose`: Integer
- `BloodPressure`: Integer
- `SkinThickness`: Integer
- `Insulin`: Integer
- `BMI`: Float
- `DiabetesPedigreeFunction`: Float
- `Age`: Integer

### Example Request

Alternatively, instead of Swagger UI, you can directly enter the following URL into your browser with the parameters you want:

```
https://diabetes-prediction-model-5d9550a8d37f.herokuapp.com/api/diabetes_prediction?pregnancies=2&Glucose=120&BloodPressure=80&SkinThickness=20&Insulin=85&BMI=25.5&DiabetesPedigreeFunction=0.5&Age=33
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

Ensure that you install all dependencies listed in `requirements.txt` before running the project.

## Running Locally

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/dev-achintha/-test-ML_Model_Deployement_using_Fast_API.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

4. Visit `http://127.0.0.1:8000/docs` in your browser to interact with the API using the FastAPI Swagger UI.
