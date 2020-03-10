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


x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]
AND = Perceptron(0.5, 0.5, 0.7)
NAND = Perceptron(-0.5, -0.5, -0.7)
OR = Perceptron(0.5, 0.5, 0.4)
for (x1, x2) in zip(x1_list, x2_list):
    print("AND("+str(x1)+","+str(x2)+") = "+str(AND.forward(x1, x2))+"  ", end='')
    print("NAND("+str(x1)+","+str(x2)+") = "+str(NAND.forward(x1, x2))+"  ", end='')
    print("OR("+str(x1)+","+str(x2)+") = "+str(OR.forward(x1, x2))+"  ", end='')
    print('')

