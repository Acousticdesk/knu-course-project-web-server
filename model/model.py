import pandas as pd
import os

path = os.path.join(os.getcwd(), 'model', 'lm_HPRICE7.pickle')
# path = './lm_HPRICE7.pickle'
lm_HPRICE7 = pd.read_pickle(path)
