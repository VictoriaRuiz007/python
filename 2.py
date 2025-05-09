import random

print("Bienvenido a adivina al numero")
print("A continuacion, deberas ingresar dos limites para adivinar")

#ingreso datos
limite_1 = int(input("Limite 1: "))
limite_2 = int(input("Limite 2: "))

while limite_1 > limite_2:
    limite_1 = int(input("Ingrese el limite 1 de nuevo: "))
    limite_2 = int(input("Ingrese el limite 2 de nuevo: "))


#generacion aleatorio
num_secreto = random.randint(limite_1, limite_2)
print("")
#juego
print("El numero aleatorio ha sido generado, ahora te toca adivinarlo")
print("Posees 3 intentos para esto")
print("")


#funciones
def msj_fallo():
    print("Numero incorrecto")

def msj_mayor():
    if intento1 < num_secreto or intento2 < num_secreto or intento3 < num_secreto:
        print("El numero secreto es mayor")

def msj_menor():
    if intento1 > num_secreto or intento2 > num_secreto or intento3 > num_secreto:
        print("El numero secreto es menor")

def msj_ganador():
    print("Has adivinado, el numero era ", num_secreto)


#intentos

#1
intento1 = int(input("Ingresa tu primer intento: "))
if intento1 == num_secreto:
    msj_ganador()
elif intento1 > num_secreto:
    msj_menor()
elif intento1 < num_secreto:
    msj_mayor()

#2
intento2 = int(input("Ingresa tu segundo intento: "))
if intento2 == num_secreto:
    msj_ganador()
elif intento2 > num_secreto:
    msj_menor()
elif intento2 < num_secreto:
    msj_mayor()

#acercamientos intento 2

acerc_1 = num_secreto - intento1
acerc_2 = num_secreto - intento2

print("")
if acerc_1 > acerc_2:
    print("El intento 2 está mas cerca del número secreto")
else:
    print("El intento 1 está mas cerca del número secreto")


#3
intento3 = int(input("Ingresa tu ultimo intento: "))
if intento3 == num_secreto:
    msj_ganador()
else:
    print("Has acabado tus intentos, el numero era ", num_secreto)








# programa que permita ingresar dos numeros q actuen como rango. primer valor debe ser menor
# que el segundo. luego, debe generar un numero aleatorio entre estos dos.
# 3 intentos, si se falla en el primero, debe indicar si el numero es mayor o menor. en el
# segundo intento, debe indicar qué intento estaba mas cerca y si es mayor o menor. al tercer
# intento, si  no adivina, debe decir perdiste. si acierta en cualquier intento, debe escribir
# adivinaste