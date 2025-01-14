print("Promedio de calificaciones")


calificaciones_n= int(input("Ingresa la cantidad de calificaciones: "))


calificaciones2=[]

for i in range(calificaciones_n):
    
    calificacion = float(input(f"Ingresa la calificacion {i+1}: "))
    calificaciones2.append(calificacion)

promedio = sum(calificaciones2) / len(calificaciones2)

print(f"El promedio de las calificaciones es: {promedio}")
    

