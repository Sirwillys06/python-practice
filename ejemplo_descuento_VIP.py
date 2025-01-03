print("****** Sistema de descuentos VIP *******")

no_productos_descuento = 10
cantidad_productos = int(input("Cuantos productos compraste hoy?: "))
tiene_membresia = input("Tienes membresia VIP? (si/no): ")

descuento_aprobado = (cantidad_productos >=no_productos_descuento and tiene_membresia.lower().strip() == "si")

print("Descuento aprobado: " + str(descuento_aprobado))
