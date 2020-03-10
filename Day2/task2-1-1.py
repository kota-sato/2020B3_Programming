class Perceptron():
    def __init__(self, a, b, c):
        self.w1= a
        self.w2= b
        self.theta = c

    def forward(x1, x2):
        if w1 * x1 + w2 * x2 < theta:
            return 0
        else :
            return 1