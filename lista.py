print("Hola, bienvenido. Porfavor escriba su lista en una cantidad de 5 objetos")

obj1 = input("Producto 1: ")
obj2 = input("Producto 2: ")
obj3 = input("Producto 3: ")
obj4 = input("Producto 4: ")
obj5 = input("Producto 5: ")

lista = [obj1, obj2, obj3, obj4, obj5]
print("A continuación, su lista: ")
print("-", lista[0])
print("-", lista[1])
print("-", lista[2])
print("-", lista[3])
print("-", lista[4])

print("¿Desea eliminar algún elemento?")
eleccion = input("Escriba si o no")
if eleccion == "si":
    print("Elija que elemento desea eliminar")
    print("1-", obj1)
    print("2-", obj2)
    print("3-", obj3)
    print("4-", obj4)
    print("5-", obj5)
    numero = input("Seleccione un numero")
    if numero == "1":
        del lista[0]
    if numero == "2":
        del lista[1]
    if numero == "3":
        del lista[2]
    if numero == "4":
        del lista[3]
    if numero == "5":
        del lista[4]

    print("Sus productos quedarian asi")
    print(lista)
    
if eleccion == "no":
    print("Entendido, muchas gracias")















#lista de supermercado: mostrar msj bienvenida. agregar los productos. mostrar msj de añade tu producto. solicitar modificar productos o eliminar alguno. imprimir lista