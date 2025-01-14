print("Play List canciones")

# Definir una lista de canciones
Lista_reproduccion = []



#Agregar canciones a la lista por medio de la consola 

numero_canciones = int(input("Cuantas canciones desea agregar a la lista de reproduccion: "))


for i in range(numero_canciones):
    cancion = input(f"Ingrese el nombre de la cancion {i +1 }: ")
    Lista_reproduccion.append(cancion)

#Orfenar la lista de reproduccion con el metodo sort

Lista_reproduccion.sort() #Ordena la lista de reproduccion en orden alfabetico ascendente
#si agregamos el parametro reverse=True, ordena la lista de reproduccion en orden alfabetico descendente

#Mostrar la lista iterando los elementos:

for cancion in Lista_reproduccion:
    print(cancion)