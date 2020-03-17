import numpy as np
import Day2.relu
from Day2.relu import *


class SingleLayer:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def forward(self, x):
        return relu(np.dot(x, self.w) + self.b)


x = np.array([1.0, 0.5])
w = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

if __name__ == "__main__":
    single_layer = SingleLayer(w, b)
    print(single_layer.forward(x))

