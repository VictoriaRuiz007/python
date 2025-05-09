print("Bienvenido a nuestra institución")
print("A continuación, podrá calcular sus beneficios a partir de los datos que usted entregue")
print("")

promedio = float(input("Ingrese su promedio de notas: "))
print("")
quintil = int(input("Ingrese su quintil socioeconómico del 1 al 5: "))

#variables modificables
arancel = 1800000
matricula = 90000

#descuentos
dcto_arancel = 0
dcto_matricula = 0

#condiciones arancel
if promedio > 6 and quintil == 1 or quintil == 2:
    dcto_arancel += 0.2

elif promedio > 6 and quintil == 3 or quintil == 4:
    dcto_arancel += 0.15

elif promedio > 5 and promedio <= 6 and quintil == 1 or quintil == 2:
    dcto_arancel += 0.13

elif promedio > 5 and promedio <= 6 and quintil == 3 or quintil == 4:
    dcto_arancel += 0.1

#condiciones matrícula
if quintil == 1 or quintil == 2:
    dcto_matricula += 0.1
    pertenece = True

if pertenece == True and promedio >= 5.5:
    dcto_matricula += 0.05

#totales
total_arancel = arancel - (arancel * dcto_arancel)
total_matricula = matricula - (matricula * dcto_matricula)

#salida
print("Los descuentos han sido aplicados")
print("El valor del arancel es: ", total_arancel)
print("El valor de la matricula es: ", total_matricula)



# programa en python q permita calcular beneficios a estudiantes a base de condicion academica
# (promedio), condicion socioeconomica(quintiles 1-5), 
# condiciones:
# 1) promedio mayor a 6, quintil 1 o 2 = 20% dcto arancel
# 2) promedio mayor a 6, quintil 3 o 4 = 15% dcto arancel
# 3) promedio mayor a 5 o menor o igual a 6, quintil 1 o 2 = 13% dcto arancel
# 4) promedio mayor a 5 o menor o igual a 6, quintil 3 o 4 = 10% dcto arancel

# matricula
# bonus: si quintil 1 o 2, dcto de 10% matricula. ademas, si promedio mayor o igual a 5,5
# 5% adicional

# arancel = 1.800.000
# matricula = 90.000