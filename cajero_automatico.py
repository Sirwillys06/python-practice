print("Cajeo automatico \n")


saldo= 0



while True:
    
    print("""
          
          Menu:
                1. Consultar saldo
                2. Depositar
                3. Retirar
                4. Salir
                
          """)
    opcion= int(input("Ingrese una opcion: "))
    while opcion not in [1, 2, 3, 4]:
            print("Opcion invalida")
            opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("Saldo actual: ", saldo)
    elif opcion ==2:
            deposito= float(input("Ingrese la cantidad a depositar: "))
            saldo += deposito
            print("Deposito exitoso")
            print("Saldo actual: ", saldo)
    elif opcion == 3:
            retiro= float(input("Ingrese la cantidad a retirar: "))
            if retiro > saldo:
                print("Fondos insuficientes")
            else:
                saldo -= retiro
                print("Retiro exitoso")
                print("Saldo actual: ", saldo)
    elif opcion == 4:
            print("Gracias por utilizar nuestros servicios")
            break