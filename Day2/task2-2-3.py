import numpy as np


class SingleLayer:
    def __init__(self, x, w, b):
        self.x = x
        self.w = w
        self.b = b

    def forward(self):
        y = b
        for (row_w, num_x) in zip(self.w, self.x):
            for (j, num_w) in enumerate(row_w):
                  y[j] = y[j] + num_w * num_x
        print(y)


x = np.array([1.0, 0.5])
w = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

single_layer = SingleLayer(x, w, b)
single_layer.forward()

