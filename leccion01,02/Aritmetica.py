class Aritmetica:

  def __init__(self, operandoA, operandoB):
    self.operandoA = operandoA
    self.operandoB = operandoB


  def sumar(self):
    return self.operandoA + self.operandoB

  def restar(self):
    return self.operandoA - self.operandoB

  def multiplicar(self):
    return self.operandoA * self.operandoB

  def dividir(self):
    return self.operandoA / self.operandoB


Aritmetica1 = Aritmetica(5,3)
print (f"sumar: {Aritmetica1.sumar()}")
print (f"restar: {Aritmetica1.restar()}")
print (f"multiplicar: {Aritmetica1.multiplicar()}")
print (f"dividir: {Aritmetica1.dividir():.2f}")