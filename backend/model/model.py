from tensorflow.keras.models import load_model
import sklearn
import pickle
import json
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path to your pickle file relative to the script's directory
final_pipeline_path = os.path.join(script_dir, 'final_pipeline.pkl')
Drop_Columns_path = os.path.join(script_dir, 'Drop_Columns.txt')
best_model_path = os.path.join(script_dir, 'best_model.h5')

# Open and load the pickle file
with open(final_pipeline_path, 'rb') as file_1: 
  final_pipeline = pickle.load(file_1)
with open(Drop_Columns_path,'r') as file_2:
  Drop_Columns = json.load(file_2)

best_model = load_model(best_model_path)