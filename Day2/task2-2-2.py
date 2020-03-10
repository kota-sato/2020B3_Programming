import numpy as np


def relu(x):
    y = x
    for i, num in enumerate(x):
        if 0 > num:
            y[i] = 0
        else:
            y[i] = num
    print(y)


x = np.array([-1.0, 0.0, 0.5, 2.0])

relu(x)

