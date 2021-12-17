import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def leer_numero_empleados():
  numero=int(input("Cantidad de empleados: "))
  return numero

def leer_ventas_empleados_mes():
  empleados=leer_numero_empleados()
  lista_empleados=[]
  cont= 1
  while cont <= empleados:
    emp=input(f"Empleado numero {cont}: ")
    lista_empleados.append(emp)
    cont+=1
  print(lista_empleados)  
  lista_meses=["ENERO,FEBRERO,MARZO","ABRIL,MAYO,JUNIO","JULIO,AGOSTO,SEPTIEMBRE","OCTUBRE,NOVIEMBRE,DICIEMBRE"]
  
  matriz_ventas={"NOMBRE":lista_empleados}
  
  for x in lista_meses:
    lista=[]
    num=len(lista_empleados)
    def recursiva(num):
      if num > 0:
        recursiva(num-1)
        venta=int(input(f"Ventas de {x} del vendedor {lista_empleados[num-1]}: "))
        
        lista.append(venta)
    recursiva(num)
    
    matriz_ventas.update({x:lista})

  return matriz_ventas, lista_empleados

def ordenar_vendeores_por_ventas():
  matriz, lista=leer_ventas_empleados_mes()
  totalventas=[]
  num2=len(lista)
  def recursiva2(num2):
    if num2>0:
      recursiva2(num2-1)
      total_ventas=[matriz["ENERO,FEBRERO,MARZO"][num2-1],matriz["ABRIL,MAYO,JUNIO"][num2-1],matriz["JULIO,AGOSTO,SEPTIEMBRE"][num2-1],matriz["OCTUBRE,NOVIEMBRE,DICIEMBRE"][num2-1]]
      totalisimo=sum(total_ventas)
      totalventas.append(totalisimo)
      
  recursiva2(num2)
  matriz.update({"TOTAL VENTAS":totalventas})
  return matriz
  


def calcular_cinco_vendedores():
  matriz2=ordenar_vendeores_por_ventas()
  tabla=pd.DataFrame(matriz2)
  ordenar=tabla.sort_values("TOTAL VENTAS", ascending = False)
  print("==============MEJORES VENDEDORES======================\n")
  print(ordenar)
  return matriz2
  

def calcula_mes_mas_ventas():
  matri=calcular_cinco_vendedores()
  
  
  MES1=sum(matri["ENERO,FEBRERO,MARZO"])
  MES4=sum(matri["ABRIL,MAYO,JUNIO"])
  MES7=sum(matri["JULIO,AGOSTO,SEPTIEMBRE"])
  MES10=sum(matri["OCTUBRE,NOVIEMBRE,DICIEMBRE"])

  ventas_meses=[MES1,MES4,MES7,MES10]

  lista_meses=["ENERO,FEBRERO,MARZO","ABRIL,MAYO,JUNIO","JULIO,AGOSTO,SEPTIEMBRE","OCTUBRE,NOVIEMBRE,DICIEMBRE"]

  mayor=max(ventas_meses)

  mayorr=ventas_meses.index(mayor)
  print
  print("=======================================================\n")
  print(f"Trimestre de mayores ventas: {lista_meses[mayorr]}")

  return ventas_meses


def graficar_ventas_por_mes():
  
  ventas=calcula_mes_mas_ventas()
  lista_meses=["1er trimestre","2do trimestre","3er trimestre","4to trime"]
  x= np.array(lista_meses)
  y= np.array(ventas)

  plt.bar(x,y)
  plt.show()
  