import numpy as np


def sigmoid(x):
    y = x
 #   for i, word in enumerate(my_list):
    for i, num in enumerate(x):
        y[i] = (1 / (1 + np.exp(-num)))
    print(y)


x = np.array([-1.0, 0.0, 0.5, 2.0])

sigmoid(x)

