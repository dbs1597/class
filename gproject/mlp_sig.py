import numpy as np


def actf(x): # 활성화 함수(sigmoid)
    return 1.0 / (1.0 + np.exp(-x))


def actf_deriv(x): # 활성화 함수 미분
    return x * (1 - x)


# 입력유닛 개수, 은닉층유닛 개수, 출력유닛 개수
inputs, hiddens, output = 2, 2, 1
learning_rate = 0.3

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 입력샘플
T = np.array([[0], [1], [1], [0]])              # 정답

W1 = np.array([[0.10, 0.20], [0.30, 0.40]])     # 은닉층으로 가는 가중치
W2 = np.array([[0.50], [0.60]])                 # 출력층으로 가는 가중치
B1 = np.array([0.1, 0.2])                       # 은닉층으로 가는 바이어스값
B2 = np.array([0.3])                            # 출력층으로 가는 바이어스값

def predict(x):
    layer0 = x
    Z1 = np.dot(layer0, W1) + B1                # np.dot => 행렬곱
    layer1 = actf(Z1)
    Z2 = np.dot(layer1, W2) + B2
    layer2 = actf(Z2)
    return layer0, layer1, layer2


def test():
    for x, y in zip(X, T):
        x = np.reshape(x, (1, -1))
        layer0, layer1, layer2 = predict(x)
        print(x, y, layer2)


def fit():
    global W1, W2, B1, B2
    for i in range(10000):
        # if i % 10000 == 0:
        #     print(i/10000)
        for x, y in zip(X, T):
            x = np.reshape(x, (1, -1))
            y = np.reshape(y, (1, -1))

            layer0, layer1, layer2 = predict(x)
            layer2_error = layer2 - y
            layer2_delta = layer2_error * actf_deriv(layer2)
            layer1_error = np.dot(layer2_delta, W2.T)
            layer1_delta = layer1_error * actf_deriv(layer1)

            W2 += -learning_rate * np.dot(layer1.T, layer2_delta)
            W1 += -learning_rate * np.dot(layer0.T, layer1_delta)
            B2 += -learning_rate * np.sum(layer2_delta, axis = 0)
            B1 += -learning_rate * np.sum(layer1_delta, axis = 0)


fit()
test()