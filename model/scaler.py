import joblib
import os

scaler_x_path = os.path.join(os.getcwd(), 'model', 'scaler_x.save')
scaler_y_path = os.path.join(os.getcwd(), 'model', 'scaler_y.save')

scaler_x = joblib.load(scaler_x_path)
scaler_y = joblib.load(scaler_y_path)
