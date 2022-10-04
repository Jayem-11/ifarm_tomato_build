import uvicorn
import numpy as np
from io import BytesIO
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = tf.keras.models.load_model("../models/model.h5")
CLASS_NAMES = ["Bacterial_spot", "Early blight", "Late blight","Leaf Mold","Septoria Leaf spot","Spider mites two spotted spider mite","Target_spot", "YellowLeaf Curl virus","Mosaic virus","healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile):
    image = read_file_as_image(await file.read())

    image_batch = np.expand_dims(image, 0)
    predictions = MODEL.predict(image_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        'class': predicted_class,
        "confidence": float(confidence)
    }
