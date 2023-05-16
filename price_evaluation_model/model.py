import pandas as pd
import os

path = os.path.join(os.getcwd(), 'price_evaluation_model', 'lm_HPRICE10.pickle')
# path = './lm_HPRICE10.pickle'
lm_HPRICE10 = pd.read_pickle(path)
