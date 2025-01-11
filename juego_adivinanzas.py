from random import randint

numero= randint(1,50)
contador= 0
adivinanza= None

print("Adivina el número entre 1 y 50 \n")



while adivinanza != numero:
    adivinanza= int(input("Introduce un número: "))
    
    if adivinanza < numero:
        print("El número es mayor")
    elif adivinanza > numero:
        print("El numero es menor")
    contador += 1
    if contador == 3 :
        print("Has fallado 3 veces")
        break

else:
    print("Felicidades, has adivinado el número en ", contador, " intentos")


    
