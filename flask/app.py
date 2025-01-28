from fastapi import FastAPI, HTTPException
from flask import Flask, request
from flask_cors import CORS  # Import CORS

from pydantic import BaseModel
from transformers import AutoTokenizer, BertForSequenceClassification
import torch
import os
# Initialize FastAPI
app = Flask(__name__)
CORS(app)
# Load the tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # Use the base model tokenizer
except Exception as e:
    raise RuntimeError(f"Error loading tokenizer: {e}")

# Load the model manually
try:
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
    path_to_model = os.path.join(os.getcwd(), "data/model/model1.pth")
    model.load_state_dict(torch.load(path_to_model))
    model.eval()
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Define the input data schema
class InputText(BaseModel):
    text: str

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.json
        print(data)
        data = data.get('data')
    try:
        inputs = tokenizer(data, return_tensors="pt", truncation=True, max_length=128)
        with torch.no_grad():
            outputs = model(**inputs)
            probabilities = torch.softmax(outputs.logits, dim=-1)
        human_prob = probabilities[0][0].item() * 100
        ai_prob = probabilities[0][1].item() * 100
        result = {"Human": round(human_prob, 2), "AI": round(ai_prob, 2)}
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
    

if __name__ == "__main__":
    app.run()