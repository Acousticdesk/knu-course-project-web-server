from tensorflow import keras
import os

path = os.path.join(os.getcwd(), 'class_evaluation_model', 'class_evaluation_model')
# path = './class_evaluation_model'
class_evaluation_model = keras.models.load_model(path)
