inicial= True

while inicial:
    print("Menu interactivo \n")
    
    print(
    """
    Menu:
        1. crear cuenta
        2. elimnar cuenta
        3. salir
    """)
    opcion= int(input("Ingrese una opcion: "))
    if opcion == 1:
        print("Creando cuenta...\n")
    elif opcion == 2:
        print("Eliminando cuenta...\n")
    elif opcion == 3:
        print("Saliendo...\n")
        inicial= False
    else:
        print("opcion invalida\n")
    
    
    
    
    
    
