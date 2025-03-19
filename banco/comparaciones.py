class A:
    def __init__(self):
        self.valor = 3

    def __eq__(self, otro):
        print("Se llama al __eq__ de A")
        return self.valor == otro.valor


class B(A):
    def __init__(self):
        super().__init__()
        self.valor = 4

    def __eq__(self, otro):
        print("Se llama al __eq__ de B")
        return self.valor == otro.valor

a, b = A(), B()
b == b
