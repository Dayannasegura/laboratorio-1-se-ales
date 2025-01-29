# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:31:51 2025

@author: DELL
"""

print("Hola mundo")


x=-5

if x>4:
    print ("X es mayor a 4")
elif x==4:
    print("X es igual a 4")
else:
    print("X es menor 4")  

for i in range(40):
    print(i)

nombres = ["David", "Dayanna", "Ana", "Jhonathan"]

for i in nombres:
    print(i)

for i in "Fresa":
    print(i)
    

y = int(input("Ingrese un numero para sumar: "))
print(f"Tu numero es: {y}")
z = int(input("Ingrese un numero para sumar: "))
print(f"Tu numero es: {z}")



def suma (N,M):
    return N+M
resultadosuma = suma(y,z)
print(f"la suma de los dos valores es: {resultadosuma}")
print (min(nombres))

numeros = [2,5,98,2,42,6,13]
print (max(numeros))


"""
Tipo de switch 1

match opcion:
    case 1:
        print("Opcion 1")
    case 2:
         print ("Opcion 2")
    case _:
         print ("No existe la opcion")

Tipo de switch 2

opcion = int(input ("Ingrese la opcion: "))

if opcion == 1:
    print ("Opcion 1")
elif opcion == 2:
    print ("Opcion 2")
elif opcion == 3:
    print ("Opcion 3")
"""

def opcion1():
    return "Opcion 1"
def opcion2():
    return "Opcion 2"
def opcion3():
    return "Opcion 3"

switch = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    }

opcion = int(input ("Ingrese la opcion: "))
j = switch.get(opcion, lambda: "Opcion no valida")()
print (j)












