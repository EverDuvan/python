class Cubo:
  def __init__(self, ancho, profundidad, altura):
    self.ancho = ancho
    self.profundidad = profundidad
    self.altura = altura


  def volumen(self):
    return self.ancho * self.profundidad * self.altura

ancho = int(input ("x:"))
profundidad = int(input ("y:"))
altura = int(input ("z:"))

Cubo1 = Cubo(ancho, profundidad, altura)

print (f"El volumen del cubo es de: {Cubo1.volumen()}")