titulos = []
ejemplares = []


i = 0
while True:
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
        consulta_titutlo = input("Que titulo desea buscar: ").lower()
        for consulta_titulo in titulos:
