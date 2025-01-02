#Generador de Emails.

print("Generador de Emails \n")

nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
nombre_empresa= input("Ingrese el nombre de la empresa: ")
dominio= input("Ingrese el dominio de la empresa: ")


#Normalizacion de variables
nombre_usuario= nombre.lower().replace(" ", ".").strip()

apellido_usuario= apellido.lower().replace(" ", ".").strip()

nombre_empresa_normalizado= nombre_empresa.lower().replace(" ", "").strip()
dominio= dominio.strip().lower().replace(" ", "")   

email_final= f"{nombre_usuario}.{apellido_usuario}@{nombre_empresa_normalizado}{dominio}"

print(f"""
      
      Hola {nombre}
      el email generado por el sistema es: {email_final}
      
    
      """)

