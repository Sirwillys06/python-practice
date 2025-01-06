nombre= input("Ingrese su nombre: ")
dias_estadia= int(input("Ingrese la cantidad de dias de estadia: "))
vista_mar= input("¿Desea una habitacion con vista al mar? (si/no): ")

precio_vista_mar= 100.40
precio_no_vista_mar= 50.90

total_estadia_vista_mar= precio_vista_mar * dias_estadia
total_estadia_no_vista_mar= precio_no_vista_mar * dias_estadia

if vista_mar.strip().lower() == "si":
    print(f"""
          nombre: {nombre}
          dias de estadia: {dias_estadia}
         costo por dia con vista al mar: {precio_vista_mar}   
          El total a pagar por la estadia con vista al mar es de: ${total_estadia_vista_mar}
          
          """)
else:
    print(f"""
           nombre: {nombre}
          dias de estadia: {dias_estadia}
         costo por dia sin vista al mar: {precio_no_vista_mar}   
          El total a pagar por la estadia sin vista al mar es de: ${total_estadia_no_vista_mar}
          
          """)