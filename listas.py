print("manejo de listas")

# Crear una lista
lista= [1,2,3,4,5,6,7,8,9,10]

# Imprimir la lista
print(lista)

#largo de una lista con len
print(len(lista))

#accedeer a un elemento de la lista por los idices:
print(lista[0]) 
print(lista[1])
print(lista[6])

#modifiacar los elemetos  de una lista:
lista[0]=100 
print(lista)

#agregar elementos a una lista
lista.append(200) #se agrega el elemento al final de la lista
print(lista)

#Añadir un nuevo elemento en uun indice especifico de la lista
lista.insert(2,300) #el dos corresponde a la posicion en la que se va a agregar el elemento
print(lista)

#eliminar elementos de una lista
lista.remove(100) #se elimina el elemento 100 de la lista
print(lista)

#eliminar un elemento con el indice, medoto POP
lista.pop(0) #se elimina el elemento en la posicion 0
print(lista)

#eliminar un elemento con la palabra reservada del
del lista[0] #se elimina el elemento en la posicion 0
print(lista)


#Obtener sublistas:
sublista= lista[0:3] #se obtiene los elementos de la posicion 0 a la 3 sin incluir el 3
print(sublista)