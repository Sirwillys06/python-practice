calificacion= int(input("Ingrese la calificación (entre 0 y 10): "))

while calificacion < 0 or calificacion > 10:
    print("La calificación ingresada no es válida")
    calificacion= int(input("Ingrese la calificación (entre 0 y 10): "))
    
if calificacion >= 9 and calificacion <=10:
    print("A")
elif calificacion >= 8 and calificacion <=9:
    print("B")
elif calificacion >= 7 and calificacion <=8:
    print("C")
elif calificacion >= 6 and calificacion <=7:
    print("D")
else:
    print("F")