import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
print(X)
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([[1], [2]])) + 3
print(y)
reg = LinearRegression().fit(X, y)
# print(reg)
