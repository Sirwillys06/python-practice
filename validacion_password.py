print("Validacion Contraseña")

contraseñ= input("Porfavor ingrese una contraseña con minimo 6 caracteres: ")
while len(contraseñ) < 6:
    contraseñ = input("Contraseña no valida, porfavor ingrese una contraseña con minimo 6 caracteres: ")
print("Contraseña valida")