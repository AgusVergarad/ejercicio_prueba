


registro= 0

while (registro== 0):
    try:
        cientifico= -1
        cientifico= int(input("¿Cuantos cientificos desea ingresar? "))
        if cientifico <=0:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
        else:
            registro +1
        
    except ValueError:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
        registro= 0

investigadoresPrincipales= 0
investigadoresAsistentes= 0

for i in range(cientifico):
    print(f"Registro cientifico: {i + 1}")

    idCientifico= input("Ingrese el id cientifico: ").strip()
    while(len(idCientifico))< 12 or " " in idCientifico:
        print("Error. El id debe tener al menos 12 caracteres y no incluir espacios")
        idCientifico= input("Ingrese el id cientifico: ").strip()






