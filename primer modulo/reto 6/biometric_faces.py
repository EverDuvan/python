
def preguntar(titulo, opciones, campos):
  respuesta = 0
  while respuesta <= 0 or respuesta > len(opciones):
    contador = 0
    for opcion in opciones:
      contador += 1
      if campos == 1:
        print(f"\n{contador}. {opcion}.")
      elif campos == 2:
        print(f"\n{contador}. {opcion[0]}: {decodificar(opcion[1])} .")
    try:
      respuesta = int(input(f"{titulo}: "))
    except:
      respuesta = 0
    if respuesta <= 0 or respuesta > len(opciones):
      print("\nRespuesta incorrecta, intenta de nuevo...\n")
    else:
      return respuesta

def decodificar(aspectoCodificado):
  result = ""
  enProceso = []
  for caracter in aspectoCodificado:
    if len(enProceso) < 2:
      enProceso.append(caracter)
    if len(enProceso) == 2:
      for i in range(0,int(enProceso[0])):
        result += enProceso[1]
      enProceso = []
  return result

def imprimirRostro(rostroCodificado):
  for rasgo in rostroCodificado:
    print(decodificar(rasgo))
  print("\n")

def agregarRostro(rostros):
  rostroActual = []
  rostroActual.append(cabellos[preguntar("Elige un cabello", cabellos, 2)-1][1])
  print("\nEl rostro va asi:\n")
  imprimirRostro(rostroActual)
  rostroActual.append(ojos[preguntar("Elige los ojos", ojos, 2)-1][1])
  print("\nEl rostro va asi:\n")
  imprimirRostro(rostroActual)
  rostroActual.append(nariz[preguntar("Elige la nariz y orejas", nariz, 2)-1][1])
  print("\nEl rostro va asi:\n")
  imprimirRostro(rostroActual)
  rostroActual.append(bocas[preguntar("Elige la boca", bocas, 2)-1][1])
  print("\nEl rostro va asi:\n")
  imprimirRostro(rostroActual)
  rostroActual.append(menton[preguntar("Elige el mentón", menton, 2)-1][1])
  print("\nEl rostro queda asi:\n")
  imprimirRostro(rostroActual)

  pausa()

  dia = preguntar("Elige un dia de la semana para este rostro", ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"], 1)
  id = input("\nAdvertencia, si introduces un ID existente este sera sobre-escrito.\nIngresa un ID para este rostro: ")
  rostros.append({
    "id": id,
    "rostro": rostroActual,
    "dia": dia
  })

  print(f"ID: {id}")
  print(f"Dia de la semana: {dia}")
  print("Rostro:\n")
  imprimirRostro(rostroActual)
  print("\nRostro agregado exitosamente.")
  pausa()

  return rostros

def buscarPorLlave(llave, valor):
  resultado = []
  for rostro in rostros:
    if rostro[llave] == valor:
      resultado.append(rostro)
  return resultado

def pausa():
  input("\nPresiona ENTER para continuar")

rostros = []

cabellos = [
  ["Pelo denso","1 9W"],
  ["Pelo escaso","1 9|"],
  ["Rapado",'1 1|7"1|'],
  ["A raya","1 3\\6/"],
]
ojos = [
  ["Ojos grandes","1 1|2 1o1 1o2 1|"],
  ["Ojos pequeños","1 1|1-1(1.1 1.1)1-1|"],
  ["Ojos con lentes",'1 1|1-1(1o1 1o1)1-1|'],
  ["Ojos chinos","1 1|2 1\\1 1/2 1|"],
]
nariz = [
  ["Tipo 1","0 1@4 1J4 1@"],
  ["Tipo 2","0 1{4 1\"4 1}"],
  ["Tipo 3",'0 1[4 1j4 1]'],
  ["Tipo 4","0 1<3 3-3 1>"],
]
bocas = [
  ["Boga gruesa","1 1|2 3=2 1|"],
  ["Boca pequeña","1 1|3 1-3 1|"],
  ["Boca caída",'1 1|2 3_2 1|'],
  ["Boca alzada","1 1|2 3-2 1|'"],
]
menton = [
  ["Normal","2 1\\5_1/"],
]
#Funcion Menu para seleccionar
while True:
  try:
    print("============= Guerra Digital 4 =============")
    opcionMenu = preguntar("\n==== Selecciona una opción:", ["Agregar un rostro","Buscar por dia","Buscar por ID","Mostrar todo"], 1)
    if opcionMenu == 1:
      rostros = agregarRostro(rostros)
      print(rostros)
    elif opcionMenu == 2:
      dia = preguntar("Que dia de la semana deseas buscar?", ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"], 1)
      encontrados = buscarPorLlave("dia", dia)
      if len(encontrados) > 0:
        contador = 0
        for resultado in encontrados:
          contador += 1
          print(f"\nResultado #{contador}:\n")
          imprimirRostro(resultado["rostro"])
      else:
        print("\nNo se encontraron coincidencias.\n")
      pausa()
    elif opcionMenu == 3:
      id = input("\nIngresa el ID que quieres buscar: ")
      encontrados = buscarPorLlave("id", id)
      if len(encontrados) > 0:
        contador = 0
        for resultado in encontrados:
          contador += 1
          print(f"\nResultado #{contador}:\n")
          imprimirRostro(resultado["rostro"])
      else:
        print("\nNo se encontraron coincidencias.\n")
      pausa()
    elif opcionMenu == 4:
      contador = 0
      if len(rostros) > 0:
        for resultado in rostros:
            contador += 1
            print(f"\nResultado #{contador}")
            imprimirRostro(resultado["rostro"])
      else:
        print("\nNo se encontraron coincidencias.\n")
      pausa()
  except:
    print("Un error inesperado ha ocurrido. Por favor contacte al administrador del sistema.")