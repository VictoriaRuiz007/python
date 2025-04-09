n1 = int(input ("Hola, ingrese su primer numero: "))
n2= int(input("Ingrese su segundo numero: "))


print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
opcion = int(input("Elija la operacion"))

if opcion == 1:
    resultado = n1 + n2
    print ("Tu resultado es: ", resultado)

if opcion == 2:
    resultado = n1 - n2
    print ("Tu resultado es: ", resultado)

if opcion == 3:
    resultado = n1 * n2
    print ("Tu resultado es: ", resultado)

if opcion == 4:
    resultado = n1 / n2
    print ("Tu resultado es: ", resultado)