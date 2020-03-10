
import numpy as np


def softmax(x):
    exp_sum = 0
    for (i, num) in enumerate(x):
        exp_sum += np.exp(num)
    for (j, num) in enumerate(x):
        x[j] = np.exp(num) / exp_sum
    return x


class SingleLayer:
    def __init__(self, x, w, b):
        self.x = x
        self.w = w
        self.b = b
        self.y = b

    def forward(self):
        for (row_w, num_x) in zip(self.w, self.x):
            for (j, num_w) in enumerate(row_w):
                self.y[j] = self.y[j] + num_w * num_x
        return self.y
#        print(y)


class MLP_3Layer():
    def __init__(self, x):
        self.x = x
        self.y = x
        self.W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
        self.b1 = np.array([0.1, 0.2, 0.3])
        self.W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
        self.b2 = np.array([0.1, 0.2])
        self.W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
        self.b3 = np.array([0.1, 0.2])

    def forward(self):
        # for (x, w1, b1) in zip(self.x, self.W1, self.b1):
        for (i, x) in enumerate(self.x):
            ray1 = SingleLayer(x, self.W1, self.b1)
            ray2 = SingleLayer(ray1.forward(), self.W2, self.b2)
            self.b1 = np.array([0.1, 0.2, 0.3])
            ray3 = SingleLayer(ray2.forward(), self.W3, self.b3)
            self.b2 = np.array([0.1, 0.2])
            self.y[i] = ray3.forward()
            self.b3 = np.array([0.1, 0.2])

#            for y in self.y[i]:
            self.y[i] = softmax(self.y[i])

        print(self.y)


x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])

layers = MLP_3Layer(x)
layers.forward()

