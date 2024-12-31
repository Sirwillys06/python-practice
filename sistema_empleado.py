print("Sistema de empleado \n")

print("Porfavor ingresa la siguiente información: \n")
nombre= input("Nombre: ")
edad= int(input("Edad: "))
salario= float(input("Salario: "))
while salario <= 0:
    print("Porfavor ingresa un salario valido")
    salario= float(input("Salario: "))
cargo= input("es jefe de departamento? (SI/NO): ")
while cargo.upper() != "SI" and cargo.upper() != "NO":
    print("Porfavor ingresa una respuesta valida")
    cargo= input("es jefe de departamento? (SI/NO): ")  
    
    
print("Los datos ingresados son:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Salario: {salario}")
print(f"Jefe de departamento: {cargo.upper()}")