import numpy as np
from Day2.relu import *
x = np.array([-0.5, 0.0, 1.0, 2.0])


class Relu:
    def __init__(self):
        self.x = None

    def forward(self, x):
        self.x = x
        return relu(x)

    def backprop(self, dz):
        return np.where(self.x > 0, dz * 1, dz * 0)


my_relu = Relu()
print("順伝播出力："+str(my_relu.forward(x)))

print("逆伝播出力："+str(my_relu.backprop(1)))
