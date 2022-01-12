from logging import NullHandler
from fastapi import FastAPI, HTTPException
from datetime import datetime
import base64
import numpy as np
from PIL import Image
from io import BytesIO

from classes.return_class import ReturnModel, ReceiveImage
from utils.model.prepare_rcnn_model import prepare_rcnn_model
from utils.model.predict import predict
from utils.essential.get_datetime import get_datetime

app = FastAPI()

#predictor = prepare_rcnn_model()  # loads de model when start

@app.get("/ping")
async def ping_():
    return ReturnModel(
        datetime=get_datetime(),
        data=[],
        status=200,
        description="handshake"
    )


@app.get("/model")
async def prepare_():
    if predictor:
        return ReturnModel(
            datetime=get_datetime(),
            data=[],
            status=200,
            description="model ready"
        )

    else:
        return HTTPException(
            status_code=404,
            detail="model not found")

        
@app.post("/model")
async def predict_(img_base64: ReceiveImage):
    img = Image.open(BytesIO(base64.b64decode(img_base64.data)))
    img_to_array = np.array(img)
    print(img_to_array)
    

