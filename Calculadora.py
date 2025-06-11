# funcoes_aritmeticas

class funcoes_aritmeticas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        try:
            return self.a / self.b
        except ZeroDivisionError as er:
            print("Não existe divisão por zero!")
