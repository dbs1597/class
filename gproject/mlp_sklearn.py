import numpy as np
from sklearn.neural_network import MLPClassifier

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 입력샘플
T = np.array([0, 1, 1, 0])              # 정답

mlp = MLPClassifier(hidden_layer_sizes=(5,), activation='tanh', batch_size=1,
                    learning_rate_init=0.3, max_iter=10000)

count = 0
for i in range(100):

    MLPClassifier = ()

    mlp.fit(X, T)

    result = mlp.predict(X)
    print(result)

    if result[0] == T[0] and result[1] == T[1]\
            and result[2] == T[2] and result[3] == T[3]:
        count = count + 1

print(count/100)

# https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html