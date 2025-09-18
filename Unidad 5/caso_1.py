titulos = ["Ted","Nemo", "Titanic"]
ejemplares = ["14", "56","2"]
seguir = True

i = 0
while seguir:
    print("---BIBLIOTECA ESCOLAR---")
    print("1) Agregar titulo nueno")
    print("2) Mostrar catalogo")
    print("3) consultar cantidad de un titulo")
    print("4) Lista de titulos agotados")
    print("5) Registrar PRESTAMO")
    print("6 Registrar DEVOLUCION")
    print("0) Salir ")

    opcion = int(input("Ingrese eleccion: "))

    if opcion == 1:
        cantidad_titulos = int(input("Cuantos titulos va a ingresar?: "))
        if cantidad_titulos >= 0:
            for i in range(cantidad_titulos):
                titulos.append(input("Ingrese el titulo del libro: "))
                ejemplares.append(input("Ingrese la cantidad de ejemplares: "))
        print(titulos, ejemplares)               
    elif opcion == 2:
        while i < len(titulos):
            print(f"{titulos[i]}: {ejemplares[i]}")
            i += 1
    elif opcion == 3:
        consulta_titutlo = input("Que titulo desea buscar: ").strip()         
        index_titulo = -1
        i = 0
        while i < len(titulos):
            if titulos[i].lower() == consulta_titutlo:
                index_titulo = i
            i += 1
        if index_titulo == -1:
                print("titulo no encontrado")
        else:
            print(f"Disponibles de {titulos[index_titulo]}': {ejemplares[index_titulo]} ")
    elif opcion == 4:
        hay_agotados = 0
        i = 0 
        while i < len(titulos):
            if ejemplares[i] == 0:
                print(f"{titulos[i]}")
                hay = True
        if not hay:
            print("No hay titulos agotados")

    elif opcion == 5:
            prestar_titulo = input("Titulo a PRESTAR: ")
            index = -1
            i = 0 
            while i < len(titulos):
                if titulos[i].lower() == prestar_titulo.lower():
                    index = i
                i += 1
            if index == -1:
                print("titulo no encontrado")
            else:
                cantidad_titulos = input("Cantidad a prestar: ").strip
                cant = int(cantidad_titulos)
                ejemplares[index] = ejemplares[index] - 1
                print("Prestamo registrado exitosamente")


    elif opcion == 6:
            devolucion_titulo = input("Titulo a devolver: ")
            index = -1
            i = 0 
            while i < len(titulos):
                if titulos[i].lower() == devolucion_titulo:
                    index = i
                i += 1
                if index == -1:
                    print("Titulo no encontrado.")
                else:
                    cantidad_devolucion = input("Cantidad a devolver.").strip()
                    cantidad = int(cantidad_devolucion)
                    if cantidad < 1 :
                        print("Debe ser mas que uno")
                    else:              
                        ejemplares[index] = ejemplares[index] + cant
                        print("Devolución registrada.")

    elif opcion == 0:
        seguir = False
        print("---Fin de la ejecucion---")
        
        