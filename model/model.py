from tensorflow import keras
import os

model_path = os.path.join(os.getcwd(), 'model', 'real-estate-model-07-02-23')
model = keras.models.load_model(model_path)
