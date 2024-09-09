from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/api/diabetes_prediction')
async def diabetes_predd(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    input_list = [
        input_dictionary['pregnancies'],
        input_dictionary['Glucose'],
        input_dictionary['BloodPressure'],
        input_dictionary['SkinThickness'],
        input_dictionary['Insulin'],
        input_dictionary['BMI'],
        input_dictionary['DiabetesPedigreeFunction'],
        input_dictionary['Age']
    ]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return {'result': 'The person is not diabetic'}
    else:
        return {'result': 'The person is diabetic'}