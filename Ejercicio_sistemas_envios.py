costo_destino_nacional= 10000
costo_destino_internacional= 20000

destino= input("Ingrese el destino del paquete (nacional/internaiconal): ")
peso= int(input("Ingrese el peso del paquete en gramos: "))

if destino == "nacional":
    precio= costo_destino_nacional * peso
    print(f"El costo del envío nacional es: {precio}")
else:
    precio= costo_destino_internacional * peso
    print(f"El costo del envío internacional es: {precio}")