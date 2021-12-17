from FiguraGeometrica import *
from Color import *

class Cuadrado(FiguraGeometrica, Color):
  def __init__(self, lado, color):
    # para implementar varias clases padre se usa la siguiente sintaxis
    FiguraGeometrica.__init__(self, lado, lado)
    Color.__init__(self, color)

  def calcular_area(self):
    return self.alto * self.ancho

  def __str__(self):
    return f'area: {FiguraGeometrica.__str__(self)} {Color.__str__(self)} '
