print("Tienda Online")

name= input("Ingrese su nombre: ")

miembro= input("¿Es miembro de la tienda? (si/no): ")

compra= int(input("¿Cual es el monto de su compra?: "))

compra_minima= 1000

print("Tiene descuento: ")

if compra > compra_minima and miembro.strip().lower() == "si":
    print("faliciades, tiene un descuento del 10%")
    print(f"El monto a pagar es: {compra - compra * 0.10}")
    
elif miembro.strip().lower() == "si":
    print("feliciadades, tiene un descuento del 5%")
    print(f"El monto a pagar es: {compra - compra * 0.05}")
    
else:
    print("No tiene descuento")
    print(f"El monto a pagar es: {compra}")