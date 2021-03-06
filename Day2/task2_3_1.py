class Multiply:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x * y
        return z

    def backprop(self, dz):
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy


class Add:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x + y
        return z

    def backprop(self, dz):
        dx = dz
        dy = dz
        return dx, dy


a = 2
b = 3
c = 4
add = Add()
mul = Multiply()

jun = mul.forward(add.forward(a, b), c)
gyaku_ab, gyaku_c = mul.backprop(1)
gyaku_a, gyaku_b = add.backprop(gyaku_ab)
print("順伝播出力:"+str(mul.forward(add.forward(a, b), c)))

print("逆伝播出力 da:"+str(gyaku_a)+ ", db:"+str(gyaku_b)+ ", dc:"+str(gyaku_c))

