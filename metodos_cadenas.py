 
#Metodos de cadenas

cadena1= "Hola Mundo"
print(f"La cadena es: {cadena1}")

mayusculas = cadena1.upper() #Convierte la cadena a mayusculas
print(f"La cadena en mayusculas es: {mayusculas}")

minusculas = cadena1.lower() #Convierte la cadena a minusculas
print(f"La cadena en minusculas es: {minusculas}")

cadena2= " hola mundo "
print(f"cadena sin espacios: {cadena2.strip()}") #Elimina los espacios en blanco al inicio y al final de la cadena



#largo de una cadena: len()

cadena3= "Hola Mundo"
print(f"La cadena es: {cadena3}")

print(f"El largo de la cadena es: {len(cadena3)}") #Devuelve el largo de la cadena


#Subcadenas, manejo de subcadenas

cadena= "Hola Mundo"

subcadena1= cadena[0:4] #Extrae la subcadena que va desde la posicion 0 hasta la 4
print(f"Subcadena1: {subcadena1}")




#buscar subcadenas metodo find():
cadena2= "Hola Mundo"

indice= cadena2.find("Mundo") #Busca la subcadena "Mundo" en la cadena
print(f"La subcadena se encuentra en el indice: {indice}")


#Reemplazar subcadenas: metodo replace()

cadena3= "Hola Mundo"

print(f"La cadena es: {cadena3}")

nueva_cadena= cadena3.replace("Mundo", "Python") #Reemplaza la subcadena "Mundo" por "Python"

print(f"La nueva cadena es: {nueva_cadena}")



#separar cadenas: metodo split()

cadena4= "Hola Mundo"
lista= cadena4.split(" ") #Separa la cadena en una lista de subcadenas, utilizando el espacio como separador

print(f"La lista de subcadenas es: {lista}")

lista2= cadena4.split(",") #Separa la cadena en una lista de subcadenas, utilizando la coma como separador
print(f"La lista de subcadenas es: {lista2}")





