import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from google.cloud import aiplatform
from model.model import final_pipeline
from model.model import Drop_Columns
from model.model import best_model
import pandas as pd
import os

# Set the path to the JSON file relative to the current script
credentials_path = os.path.join(os.path.dirname(__file__), 'credentials.json')

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

project_id = "ctelkom"
location = "northamerica-northeast1"
model_id = "4747541675155390464"
endpoint_id = "4392584137337208832"

# Load your endpoint
endpoint = aiplatform.Endpoint(endpoint_name=endpoint_id
                               ,project=project_id,
                               location=location)

# Load model


app = FastAPI()

class User(BaseModel):
  user_id: str
  age: str
  gender : str
  region_category : str
  membership_category : str
  joining_date :str
  joined_through_referral : str
  preferred_offer_types : str
  medium_of_operation : str
  internet_option : str
  last_visit_time : str
  days_since_last_login : str
  avg_time_spent : str
  avg_transaction_value : str
  avg_frequency_login_days : str
  points_in_wallet : str
  used_special_discount : str
  offer_application_preference : str
  past_complaint : str
  complaint_status : str
  feedback : str

@app.get('/')
def index():
    return {'message': 'Customer Churn Prediction Application'}

@app.post('/vertexai_automl_prediction')
def vertexai_prediction(data:User):
    # Convert Pydantic model to dictionary
    instances = data.dict()
   
    # Send prediction request
    response = endpoint.predict(instances=[instances])
    
    # Extract the prediction result
    prediction_label = "Not Churn" if response.predictions[0]["scores"][1] > 0.5 else "Churn" 
    return {
        'prediction': prediction_label
    }

@app.post('/tensorflow_prediction')
def tensorflow_prediction(data:User):
    # Convert Pydantic model to dictionary
    df = pd.DataFrame([data.dict()])
    df_drop = df.drop(Drop_Columns,axis=1).sort_index()
    df_final = final_pipeline.transform(df_drop)
   
    # Prediction
    y_prediction = best_model.predict(df_final)
    
    # Extract the prediction result
    prediction_label = "Not Churn" if y_prediction == 0 else "Churn"
    return {
        'prediction': prediction_label
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)