import funciones as fn
import numpy as np


tipo1=['  WWWWWWWWW ','  |"""""""| ','  ||||||||| ','  \\\///// ','  TTTTTTTTT ','  ^^^^^^^^^ ','  ********* ','  <<<<>>>>> ']
tipo2=['  |  o o  | ','  |-(. .)-| ','  |-(o o)-| ','  | \ // | ','  |+ O O +| ','  |  ^ ^  | ','  |  $ $  | ','  | _x x_ | ']
tipo3=[' @    J    @ ',' {    "    } ',' [    j    ] ',' <    -    > ',' U    ^    U ',' *    V    * ',' =    8    = ',' O    .    O ']
tipo4=['  |  ===  | ','  |   -   | ','  |  ___  | ','  |  ---  | ','  |  -w-  | ','  | --_-- | ','  |  ...  | ','  |  (-)  | ']
tipo5=['  \_____/ ','  \__.__/ ','  \__^__/ ','  \=====/ ','  \__=__/ ','  \-----/ ','  \__I__/ ','  \*****/ ']


rostro=[]
encendido=1
i=0
Matriz1D = {}
while encendido==1:
  seleccion=fn.menu_principal()
  if seleccion=='1':
    print('seleccione el tipo de pelo: \n')
    rostro = []
    rostro.append(fn.pelo(tipo1))
    rostro.append(fn.pelo(tipo2))
    rostro.append(fn.pelo(tipo3))
    rostro.append(fn.pelo(tipo4))
    rostro.append(fn.pelo(tipo5))
    print ('')
    i+=1
    ids=input('Digite el id del rostro: \n')
    dia=input('Digite el dia de ingreso 1 a 7: ')
    print ('')
    Matriz1D[ids] = np.array(rostro) 
    #print(Matriz1D)
  elif seleccion =='2':
    x = (input('id del rostro a consultar: '))
    print (f'rostro en la base de datos {x}')
    print("==========================")
    print(Matriz1D[x])
    print ('')

  elif seleccion == '3':
    print ('ID en la base de datos: \n')
    todos_ids=Matriz1D.keys()
    print(todos_ids)
    print()

  elif seleccion == '4':
    print ('Rostros en la base de datos: \n')
    print (Matriz1D)

  elif seleccion == '5':
    dia1=[]
    dia2=[]
    dia3=[]
    dia4=[]
    dia5=[]
    dia6=[]
    dia7=[]
    if dia == '1':
      Matriz1D[dia]=np.array(rostro)
      print = (Matriz1D[dia])
      print ('dia 1')


