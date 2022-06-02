from sklearn.linear_model import Perceptron

# XOR 데이터
# X = [[0,0],[0,1],[1,0],[1,1]]
# y = [0, 0, 0, 1]

X = [[170, 80], [175, 76], [180, 70], [160, 55], [163, 43], [165, 48]]
y = [1, 1, 1, 0, 0, 0]

clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X, y)
print(clf.predict(X))