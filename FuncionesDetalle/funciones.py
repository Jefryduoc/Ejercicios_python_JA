#funciones 

def sumarDosNumeros():
    '''Esta funcion permite sumar dos números, 
    ingresados dentro de la función'''

    num1 = int(input("ingrese número 1 :  "))
    num2 = int(input("ingrese número 2 :  "))

    suma = num1 + num2

    print(f"la suma de {num1} + {num2} es = {suma}")

def sumar(a,b):
    '''Esta funcion permite sumar dos números ingresados por parámetros'''

    suma= a + b 
    return suma