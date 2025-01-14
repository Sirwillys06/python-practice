print("Contador de vocales")

texto= input("Introduce un texto: ")
texto = texto.lower()
vocales= 0

for letra in texto:
    if letra in "aeiou":
        vocales += 1
print("El número de vocales en el texto es: ", vocales)