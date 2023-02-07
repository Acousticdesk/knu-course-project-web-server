import numpy as np
from model import model
from scaler import scaler_y

X_to_predict_normalized = np.array([0.02702703, 0.10909091, 0.66666667, 0.        , 0.23076923,
        0.        , 0.5       , 0.        , 0.66666667, 0.        ,
        0.        , 0.42857143, 0.15272727, 0.        ])

y_hat = model.predict(X_to_predict_normalized.reshape(1, -1))

uah = scaler_y.inverse_transform(y_hat.reshape(1, -1))[0][-1]
print(f'Вартість нерухомості: {uah:,} грн')