import random
#se debe solicitar:
#-nombre
#-apellido
#año de nacimiento (yyyy)

#tomar las dos primeras letras del nombre y aplellido y convertirlas a mayusculas.
#tomar los dos ultimos digitos del año de nacimiento
#generar un digito aleatorio de 4 digitos

print("********Generador de ID*******")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
anio = input("Ingrese su año de nacimiento: ")

nombre = nombre[:2].upper().strip()
apellido = apellido[:2].upper().strip()
anio = anio[-2:].strip()

numero_aleatorio= random.randint(1000,9999)


id= nombre + apellido + anio + str(numero_aleatorio) #srt covierte el numero aleatorio a cadena


print(f"""
      Hola {nombre},
      Tu nuevo número de identificacion (ID) generado por el sistema es:
      {id}
      Felicidades!
      """)