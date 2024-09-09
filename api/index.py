from fastapi import FastAPI, Query
import pickle

app = FastAPI()

# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.get('/api/diabetes_prediction')
async def diabetes_predd(
    pregnancies: int = Query(...),
    Glucose: int = Query(...),
    BloodPressure: int = Query(...),
    SkinThickness: int = Query(...),
    Insulin: int = Query(...),
    BMI: float = Query(...),
    DiabetesPedigreeFunction: float = Query(...),
    Age: int = Query(...)
):
    input_list = [pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return {'result': 'The person is not diabetic'}
    else:
        return {'result': 'The person is diabetic'}