print("***Sistema prestamo de libros***")

name= input("Ingrese su nombre: ")
Distancia_permitida_km= 3
credencial= input("¿Tiene credencial de estudiante? (si/no): ")
distancia_vivienda= int(input("¿A cuantos km vive de la biblioteca?: "))


Admicin= credencial.strip().lower() == "si" or distancia_vivienda <= Distancia_permitida_km


print(f"""
      
      Hola {name},
      
      segun tus respuestas:
      {Admicin} para prestar un libro
      
      
      """)