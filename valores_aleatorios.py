#Valores aleatorios con la funcion randint (Devuelve numeros aleatorios enteros)

#Importamos la funcion randint
from random import randint


#generamos un numero aleatorio entre 0 y 10

numero_aleatorio = randint(0,10)
print(f"El numero aleatorio es: {numero_aleatorio}")


#simular un dado de 6 caras

dado= randint(1,6)
print(f"El numero del dado es: {dado}")