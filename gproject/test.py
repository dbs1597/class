import pandas as pd
import numpy as np
import tensorflow as tf
# from tensorflow.keras.utils import to_categorical

# 데이터 불러오기 (319795 * 18)
df = pd.read_csv('./testcsv.csv')
# print(df)

dfpandas = pd.get_dummies(df)
dfpandas.to_csv("./df_sample.csv")

# dftensor = tf.one_hot(df)

# dfkeras = to_categorical(df)