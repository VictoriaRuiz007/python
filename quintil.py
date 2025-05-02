nombre = input("Buenas, ingrese su nombre: ")
print("Bienvenido ", nombre)
edad = int(input("Ingrese su edad: "))

#condicion edad
if edad >= 65:
    bono_edad = 3000
    edad = True



#condicion empleo
empleo = input("¿Está usted trabajando actualmente?: ")
if empleo == "si":
    empleo = True
elif empleo == "no":
    empleo = False

#condiciones quintil

print("A continuacion, ingrese su quintil de ingresos")
quintil = int(input("Quintil: "))

def texto_subsidio():
    print("Su subsidio es de", subsidio)

if quintil == 1:
    subsidio = 15000
    texto_subsidio()
        
elif quintil == 2:
    subsidio = 10000
    texto_subsidio()

elif quintil == 3:
    subsidio = 8000
    texto_subsidio()

elif quintil == 4:
    subsidio = 6000
    texto_subsidio()

elif quintil == 5:
    subsidio = 1500
    texto_subsidio()

print("Al pertenecer a este quintil, usted ha recibido un bono de 2000")
if quintil == 1 or quintil == 2:
    bono_quintil = subsidio + 2000
    print("Su total hasta ahora es ", bono_quintil)

else:
    bono_quintil = subsidio 

if edad == True:
    print("Al ser mayor de 65, usted ha recibido un nono de 3000")
    total = bono_quintil + bono_edad
    print("Su total es ", total)

else:
    total = bono_quintil
    print("Su total es", total)

