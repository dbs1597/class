from audioop import bias


def calculate(input):

    global weights
    global bias

    activation = bias

    for i in range(2):
        activation += weights[i] * input[i]
        
    if activation >= 0.0:
        return 1.0
    else:
        return 0.0

def train_weights(X, y, l_rate, n_epoch):
    global weights
    global bias

    for epoch in range(n_epoch): # 에포크 반복
        sum_error = 0.0
        for row, target in zip(X, y): # 데이터셋을 반복
            actual = calculate(row) # 실제 출력 계산
            error = target - actual # 출력 오류 계산
            bias = bias + l_rate * error
            sum_error += error**2 # 오류의 제곱 계산
            for i in range(2): # 가중치 변경
                weights[i] = weights[i] + l_rate * error * row[i]
            print(weights, bias)

        print('에포크 번호=%d, 학습률=%.3f, 오류=%.3f' % (epoch, l_rate, sum_error))
    return weights

X = [[0,0],[0,1],[1,0],[1,1]]
y = [0, 0, 0, 1]

weights = [0.0, 0.0]
bias = 0.0
l_rate = 0.1
n_epoch = 5
weights = train_weights(X, y, l_rate, n_epoch)
print(weights, bias)