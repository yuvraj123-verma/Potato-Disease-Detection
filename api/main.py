from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

MODEL = tf.keras.models.load_model("../saved model")
CLASS_NAMES = ['Early_blight', 'Late_blight', 'healthy']
@app.get('/ping')
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data):
    image = np.array(Image.open(BytesIO(data)))
    img_batch = np.expand_dims(image, 0)
    pred = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(pred[0])]
    confidence = np.max(pred[0])

@app.post('/predict')
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)