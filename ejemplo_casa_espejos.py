print("Acceso a la casa de los espejos")

nombre= input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
miedo = input("¿Tiene miedo de la oscuridad? (si/no): ")

miedo2= miedo.strip().lower() == "si"

if not miedo2 and edad >= 10:
    print(f" hola {nombre} Puede ingresar a la casa de los espejos")
else:
    print("no puedes ingresa a la casa de los sustos")