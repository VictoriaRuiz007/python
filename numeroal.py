import random

print("Bienvenido a adivinar el numero")
lim_1 = int(input("Define el primer límite: "))
lim_2 = int(input("Define el segundo límite: "))

#numero
numero_secreto = random.randint(lim_1, lim_2)
numero_ajustado = round((numero_secreto/4)*4)

#juego

print("Partamos, tienes 3 intentos")

intentos = 2

numero_ingresado = int(input("Haz tu intento: "))
while intentos >= 1:
    if numero_ingresado == numero_ajustado:
        print("Felicidades! Acertaste. El numero era ", numero_ajustado)
    elif numero_ingresado > numero_ajustado:
        intentos -= 1
        print("No acertaste. El numero es menor a ", numero_ingresado, " Te quedan ", intentos, " intentos")
        numero_ingresado = int(input("Intenta de nuevo: "))
    elif numero_ingresado < numero_ajustado:
        intentos -= 1
        print("No acertase. El numero es mayor a ", numero_ingresado, " Te quedan ", intentos, " intentos")
        numero_ingresado = int(input("Intenta de nuevo: "))
else:
    print ("Te has quedado sin intentos, el numero era ", numero_ajustado)