print("****Ejemplo de receta de cocina****")

print( "Porfavor ingresa la siguuinete informaicon: \n")

nombre_receta= input("Nombre de la receta: ")
ingredientes= input("Ingredientes: ")
tiempo_preparacion= int(input("Tiempo de preparacion en minutos: "))
dificultad= input("Dificultad (Facil, Medio, Dificil): ")
while dificultad.upper() != "FACIL" and dificultad.upper() != "MEDIO" and dificultad.upper() != "DIFICIL":
    print("Porfavor ingresa una dificultad valida")
    dificultad= input("Dificultad (Facil, Medio, Dificil): ")

print("La receta es: \n")
print(f"Nombre de la receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparacion: {tiempo_preparacion} minutos")
print(f"Dificultad: {dificultad.upper()}")
