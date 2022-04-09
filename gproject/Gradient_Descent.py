x = 20
learning_rate = 0.2
precision = 0.00001
max_iterations = 100

loss_func = lambda x: (x - 3) ** 2 + 10
gradient = lambda x: 2 * x - 6

for i in range(max_iterations):
    x = x - learning_rate * gradient(x)
    print("손실함수값(", x, ")", loss_func(x))

print("최소값 = ", x)