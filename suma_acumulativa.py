#Sumar los primeros 5 numeros:

maximo= 5
numero= 1
acumulador_suma= 0

#Empeazar a iterar

while numero <= maximo:
    print(f"El valor del acumulador es: {acumulador_suma} + {numero} ")
    acumulador_suma= acumulador_suma + numero
    numero= numero + 1