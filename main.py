from typing import List
from urllib.request import Request
import tensorflow as tf
import tensorflow_text
import re
import preprocess
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import uvicorn
import numpy as np
import traceback

# Init priority instances
model = tf.saved_model.load("./saved_model")
app = FastAPI()

class RequestText(BaseModel):
    text:List[str]
    
@app.get("/")
async def index():
    return "Hello from sentiment prediction endpoint"

@app.post("/")
async def predict(req: RequestText, response: Response):
    try:
        texts = req.text
        texts = preprocess.preprocess(texts)
        prediction = model(texts)
        prediction = tf.convert_to_tensor(prediction)
        output = tf.reshape(tf.cast(tf.math.round(prediction), dtype="int32"), [len(prediction)])
        is_negative = [True if i == 0 else False for i in output]
        
        # Create a list of the prediction and the output
        real_value = [float(x[0]) for x in prediction]
        rounded = [int(x) for x in output]
        return {
            "real_value": real_value,
            "rounded": rounded,
            "is_negative": is_negative
        }
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return {"message" : "Internal Server Error"} 
    
port = 8001
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host='0.0.0.0',port=port)