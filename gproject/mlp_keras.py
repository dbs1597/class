import numpy as np
import tensorflow as tf


inputs, hiddens, output = 2, 2, 1
learning_rate = 0.3

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 입력샘플
T = np.array([[0], [1], [1], [0]])              # 정답

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=2, input_shape=(2,), activation='sigmoid'))
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
model.compile(loss='mse', optimizer=tf.keras.optimizers.SGD(lr=0.3))
model.fit(X, T, batch_size=1, epochs=10000)
print(model.predict(X))
