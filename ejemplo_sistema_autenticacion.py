usuario= "123admin"
contraseña= "admin123"

print("Sistema de autenticación")

usuario_ingresado= input("Ingrese su usuario: ")
contraseña_ingresada= input("Ingrese su contraseña: ")

if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
    print("Bienvenido al sistema")

elif usuario_ingresado != usuario:
    print("Usuario incorrecto")
    usuario_ingresado= input("Ingrese su usuario: ")
    contraseña_ingresada= input("Ingrese su contraseña: ")
    if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
        print("Bienvenido al sistema")
    else:
        print("Usuario bloqueado")
elif contraseña_ingresada != contraseña:
    print("Contraseña incorrecta")
    usuario_ingresado= input("Ingrese su usuario: ")
    contraseña_ingresada= input("Ingrese su contraseña: ")
    if usuario_ingresado == usuario and contraseña_ingresada == contraseña:
        print("Bienvenido al sistema")
    else:
        print("Usuario bloqueado")
else:
    print("usuario y contraseña invalidos, el usuario ha sido bloqueado")

    
    