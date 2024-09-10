from fastapi import FastAPI, Query, HTTPException
from pydantic import ValidationError
import pickle
import os

app = FastAPI()

# load the model
try:
    if not os.path.exists('diabetes_model.sav'):
        raise FileNotFoundError("Model file not found.")
    with open('diabetes_model.sav', 'rb') as model_file:
        diabetes_model = pickle.load(model_file)
except (FileNotFoundError, pickle.UnpicklingError) as e:
    diabetes_model = None
    print(f"Error loading model: {e}")

@app.get('/api/diabetes_prediction')
async def diabetes_predd(
    pregnancies: int = Query(..., ge=0, description="Number of pregnancies"),
    Glucose: int = Query(..., ge=0, description="Plasma glucose concentration"),
    BloodPressure: int = Query(..., ge=0, description="Diastolic blood pressure (mm Hg)"),
    SkinThickness: int = Query(..., ge=0, description="Triceps skin fold thickness (mm)"),
    Insulin: int = Query(..., ge=0, description="2-hour serum insulin (mu U/ml)"),
    BMI: float = Query(..., ge=0, description="Body mass index (weight in kg/(height in m)^2)"),
    DiabetesPedigreeFunction: float = Query(..., ge=0, description="Diabetes pedigree function"),
    Age: int = Query(..., ge=0, description="Age (years)")
):
    # check if the model loaded
    if diabetes_model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded or available.")

    # input for the model
    input_list = [pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    
    try:
        # make prediction
        prediction = diabetes_model.predict([input_list])
    except Exception as e:
        # prediction errors handling
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")

    # validate the prediction output
    if len(prediction) == 0:
        raise HTTPException(status_code=500, detail="Prediction result is empty.")

    # return the prediction result
    result = 'The person is not diabetic' if prediction[0] == 0 else 'The person is diabetic'
    return {'result': result}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return HTTPException(status_code=500, detail=f"An unexpected error occurred: {exc}")
