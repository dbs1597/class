import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# from tensorflow.keras.utils import to_categorical

# 데이터 불러오기 (319795 * 18)
df = pd.read_csv('./heart_2020_cleaned.csv')
# print(df)

# dfpandas = pd.get_dummies(df)
# print(dfpandas.columns)
# dfpandas.to_csv("./df_sample.csv")

mm_scaler = MinMaxScaler()
dfpandas = pd.get_dummies(df)
print(dfpandas)
dfpandas = mm_scaler.fit_transform(dfpandas)
print(dfpandas)
pd.DataFrame(dfpandas).to_csv('./df_sample.csv')

# dftensor = tf.one_hot(df)

# dfkeras = to_categorical(df)