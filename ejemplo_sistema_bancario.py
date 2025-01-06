# Se usa logica inversa con el operador "not"
# La lógica inversa en este programa se aplica en la condición del if.
# La variable 'salir_sistema' es True si el usuario ingresa "si" (indicando que desea salir).
# El operador 'not' invierte esta condición:
# Si 'salir_sistema' es False (el usuario no desea salir), el bloque de código dentro del if se ejecuta.
# Si 'salir_sistema' es True (el usuario desea salir), el bloque de código dentro del else se ejecuta.

print("Sistema Bancario")

salir_sistema_txt = input("¿Desea salir del sistema bancario? (si/no): ")
salir_sistema= salir_sistema_txt.strip().lower() == "si" #esta linea convierte el texto a minusculas y elimina los espacios en blanco, 
                                                         #a su vez convierte a booleano la variable salir_sistema_txt si es igual a "si"
                                                         #devuelve True, de lo contrario devuelve False
                                                         
if not salir_sistema:
    print("Continuamos en el sistema bancario")
else:
    print("Saliendo del sistema bancario")