class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Area(self):
        return self.base * self.altura


rectangulo1 = Rectangulo(10, 15)
print(f"El area del rectangulo es de: {rectangulo1.Area()}")