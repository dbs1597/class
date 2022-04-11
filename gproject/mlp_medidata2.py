import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import time


# 데이터 불러오기 (319795 * 18)
df = pd.read_csv('./heart_2020_cleaned.csv')

# 데이터 나누기
test, train = df.iloc[:106598, :], df.iloc[106598:, :]
train_class, train_var, test_class, test_var = train.iloc[:, :1], train.iloc[:, 1:], \
                                               test.iloc[:, :1], test.iloc[:, 1:]

scaler = StandardScaler()

test_class = pd.get_dummies(test_class)
test_class = test_class.drop(['HeartDisease_No'], axis=1)

test_var = pd.get_dummies(test_var)
test_var = scaler.fit_transform(test_var)

train_class = pd.get_dummies(train_class)
train_class = train_class.drop(['HeartDisease_No'], axis=1)

train_var = pd.get_dummies(train_var)
train_var = scaler.fit_transform(train_var)


start = time.time()
# mlp 모델 생성 및 실행
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=(50,), activation='sigmoid'))
model.add(tf.keras.layers.Dense(units=1, activation='relu'))
model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=0.2), metrics=["accuracy"])
model.fit(train_var, train_class, batch_size=80000, epochs=10)

print("Run time:", time.time() - start)

acc = model.evaluate(test_var, test_class)
print(acc)
