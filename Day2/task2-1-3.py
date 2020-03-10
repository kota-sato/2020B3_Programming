class Perceptron():
    def __init__(self, a, b, c):
        self.w1 = a
        self.w2 = b
        self.theta = c

    def forward(self, x1, x2):
        if self.w1 * x1 + self.w2 * x2 < self.theta:
            return 0
        else:
            return 1


def xor(x1, x2):
    n_and = Perceptron(0.5, 0.5, 0.7)
    n_nand = Perceptron(-0.5, -0.5, -0.7)
    n_or = Perceptron(0.5, 0.5, 0.4)
    return n_and.forward(n_nand.forward(x1, x2), n_or.forward(x1, x2))


x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for (x1, x2) in zip(x1_list, x2_list):
    print("XOR("+str(x1)+","+str(x2)+") = "+str(xor(x1, x2)))
