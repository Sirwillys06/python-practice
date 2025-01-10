print("calculadora")


def suma(a, b):
    return a + b
def resta (a, b):
    return a - b  
def multiplicacion (a, b):
    return a * b
def division (a, b):
    return a / b


while True:
    print(""" 
          menú:
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir
          """)
    opcion = int(input("Introduce una opción: "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("Introduce una opción válida: "))
        
    if opcion == 1:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ", suma(a, b))
        
    elif opcion ==2:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("El resultado de la resta es: ", resta(a, b))
    elif opcion ==3:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("El resultado de la multiplicación es: ", multiplicacion(a, b))
    elif opcion ==4:
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        print("El resultado de la división es: ", division(a, b))
    else:
        print("Hasta luego")
        break