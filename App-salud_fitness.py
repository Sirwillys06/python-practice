Nombre= input("Ingrese su nombre: ")
pasos = int(input("Ingrese la cantidad de pasos caminados en el dia: "))

meta_pasos_diarios= 10000
calorias_quemadas_por_paso= 0.05



if pasos <= meta_pasos_diarios:
    calorias_quemadas= pasos * calorias_quemadas_por_paso
    print(f"No llegaste a la meta diaria de pasos, caminaste {pasos} pasos y quemaste {calorias_quemadas} calorias")
elif pasos == meta_pasos_diarios:
    calorias_quemadas= pasos * calorias_quemadas_por_paso
    print(f"Felicidades, llegaste a la meta diaria de pasos, caminaste {pasos} pasos y quemaste {calorias_quemadas} calorias")
elif pasos > meta_pasos_diarios:
    calorias_quemadas= pasos * calorias_quemadas_por_paso
    print(f"Superaste la meta diaria de pasos, felicidades. caminaste {pasos} pasos y qiueamste {calorias_quemadas} calorias")
else:
    print("Ingrese una cantidad de pasos valida")