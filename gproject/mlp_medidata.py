import pandas as pd
import numpy as np
import tensorflow as tf

# 데이터 불러오기 (319795 * 18)
df = pd.read_csv('./heart_2020_cleaned.csv')
print(df)

# 데이터 나누기
train, test = df.iloc[:223856,:], df.iloc[223856:,:]
train_class, train_var, test_class, test_var = train.iloc[:,:1], train.iloc[:,1:], test.iloc[:,:1], test.iloc[:,1:]

print("train data")
print(train_class)
print(train_var)
print("test data")
print(test_class)
print(test_var)

# mlp 모델 생성 및 실행
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10, input_shape=(17,), activation='sigmoid'))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=0.2))
model.fit(train_var, train_class, batch_size=30, epochs=10000)
print(model.predict(test_var))
