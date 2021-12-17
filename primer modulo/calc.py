

def matematicas():
    cont = 0
    while cont == 0:
        opcion = int(input('digite su opcion: '))
        if opcion == 1:
            num1 = int(input("digite su primer numero: "))
            num2 = int(input("digite su segundo numero: "))
            suma = num1 + num2
            print(f"suma: {suma}")
        elif opcion == 2:
            num1 = int(input("digite su primer numero: "))
            num2 = int(input("digite su segundo numero: "))
            resta = num1 - num2
            print(f"resta: {resta}")
        elif opcion == 3:
            num1 = int(input("digite su primer numero: "))
            num2 = int(input("digite su segundo numero: "))
            multiplicacion = num1 * num2
            print(f"multiplicacion: {multiplicacion}")
        elif opcion == 4:
            num1 = int(input("digite su primer numero: "))
            num2 = int(input("digite su segundo numero: "))
            divicion = num1 / num2
            print(f"divicion: {divicion}")
        elif opcion == 5:
            cont =1
        else:
            print("numero equivocado")
    cont = 1
    return



