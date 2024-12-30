print("**Generador de emails**")


nombre_usuario = "Willys Hurtado"
nombre_usuario_normalizado= nombre_usuario.lower().replace(" ", ".")
print(f"El nombre de usuario normalizado es: {nombre_usuario_normalizado}")

nombre_empresa = "GH Stand"
nombre_empresa_normalizado= nombre_empresa.lower().strip().replace(" ", "")
dominio= ".com.co"

dominio_email= f"@{nombre_empresa_normalizado}{dominio}"
print(f"El dominio del email es: {dominio_email}")


email_final= f"{nombre_usuario_normalizado}{dominio_email}"
print(f"El email final es: {email_final}")