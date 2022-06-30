
def menu_principal():
  print("****************MENÚ*****************\n")
  print("1. DIBUJAR ROSTRO\n")
  print("2. CONSULTAR ROSTROS POR ID\n")
  print("3. CONSULTAR TODOS LOS ID'S REGISTRADOS\n")
  print("4. CONSULTAR TODOS LOS ROSTROS\n")
  print("5. GRAFICAR VACUNADOS POR DIA\n")
  select=input("Digite su opción: ")
  print ('')
  return select

def pelo(tipo):
  rpt=1
  while rpt == 1:
    cont=1
    lista1=[]

    print ('*********************opciones*********************\n')
    for i in tipo:
      print (f'opcion: {cont} {i}')
      cont+=1
    eleccion=input('ingrese su eleccion: ')
    if eleccion =='1':
      lista1.append(tipo[0])
      rpt=0
    if eleccion =='2':
      lista1.append(tipo[1])
      rpt=0
    if eleccion =='3':
      lista1.append(tipo[2])
      rpt=0
    if eleccion =='4':
      lista1.append(tipo[3])
      rpt=0
    if eleccion =='5':
      lista1.append(tipo[4])
      rpt=0
    if eleccion =='6':
      lista1.append(tipo[5])
      rpt=0
    if eleccion =='7':
      lista1.append(tipo[6])
      rpt=0
    if eleccion =='8':
      lista1.append(tipo[7])
      rpt=0
    print (f'su eleccion fue: {lista1}')
  else: 
    rpt=1
    
  return (lista1)


