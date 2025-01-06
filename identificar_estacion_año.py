mes= int(input("Ingrese el mes en valor numerico: "))

while mes < 1 or mes > 12:
    print("El mes ingresado no es válido")
    mes= int(input("Ingrese el mes en valor numerico: "))
    
if mes == 1 or 2 or 12:
    print("Invierno")
elif mes == 3 or 4 or 5:
    print("Primavera")
elif mes == 6 or 7 or 8:
    print("Verano")
else:
    print("Otoño")