import numpy as np
from Day2.task2_2_3 import *


def softmax(x):
    c = np.max(x, axis=1, keepdims=True) #何もつけないと全体のmaxをとってしまう
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a, axis=1, keepdims=True)
    y = exp_a / sum_exp_a
    return y


class SingleLayer2:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def forward(self, x):
        return softmax(np.dot(x, self.w) + self.b)


class MLP_3Layer():
    def __init__(self):
        self.W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
        self.b1 = np.array([0.1, 0.2, 0.3])
        self.W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
        self.b2 = np.array([0.1, 0.2])
        self.W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
        self.b3 = np.array([0.1, 0.2])
        self.ray1 = SingleLayer(self.W1, self.b1)
        self.ray2 = SingleLayer(self.W2, self.b2)
        self.ray3 = SingleLayer2(self.W3, self.b3)

    def forward(self, x):
        out1 = self.ray1.forward(x)
        out2 = self.ray2.forward(out1)
        out3 = self.ray3.forward(out2)
        return out3


x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])

layers = MLP_3Layer()
print(layers.forward(x))
