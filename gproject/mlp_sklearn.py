import numpy as np
from sklearn.neural_network import MLPClassifier

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 입력샘플
T = np.array([0, 1, 1, 0])              # 정답

# https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
mlp = MLPClassifier(hidden_layer_sizes=(3,), activation='tanh', batch_size=1, learning_rate_init=0.3, max_iter=10000)

MLPClassifier = ()

mlp.fit(X, T)

print(mlp.predict(X))
