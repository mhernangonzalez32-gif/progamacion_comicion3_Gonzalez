titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor","Titanic"]
ejemplares = [5, 3, 7, 5]

seguir = True
print("----BIBLIOTECA----")
while seguir:
    print("----MENU----")
    print("1) Ingresar titulos.")
    print("2) Ingresar ejemplares.")
    print("3) Mostrar catalogo.")
    print("4) consultar diponibilidad.")
    print("5) Listar agotados.")
    print("6) Agregar un titulo")
    print("7) Actualizar ejemplares (PRESTAMO/DEVOLUCION).")
    print("0) Finalizar.")

    opcion_srt = input('Ingrese una opcion: ').strip()
    if not opcion_srt.isdigit():
        print('ingrese una de las opciones validas')
        continue
    opcion_int = int(opcion_srt)
    match opcion_int:
        case 1:
            cant_new = input('Cuantos titulos desea agregar: ').strip()
            if not cant_new.isdigit():
                print('Debe ingresar un numero')
                continue
            cant_int = int(cant_new)
            if cant_int < 0:
                print('No puede ingresar un numero menor a cero')
                continue
            else:
                
                for i in range(cant_int):
                    titulo_new = input(f"Titulo N'{i+1}: ").strip().capitalize()
                    if titulo_new in titulos:
                        print('El titulo ya existe.')
                        continue
                    elif titulo_new == " ":
                        print('No puede agregar un titutlo vacio.')
                        continue
                    else:
                        titulos.append(titulo_new)
                        ejemplares.append(0)
        case 2:
            if not titulos:
                print('No hay titulos cargados.')
                continue
            print('Cuantos ejemplasres desea ingresar')
            for i in range(len(titulos)):
                cant_ejemp = input(f'{titulos[i]} - Ejemplares: ').strip()
                if not cant_ejemp.isdigit():
                    print('Debe ingresar un numero.')
                    break
                cantidad_int = int(cant_ejemp)
                if cantidad_int < 0:
                    print('La cantidad de ejemplares debe ser mayor a cero.')
                    break
                else: 
                    ejemplares[i] = cantidad_int
        case 3:
            if not titulos:
                print('No hay titulos cargados.')
                continue
            for i in range(len(titulos)):
                cant_ejemp = print(f'{titulos[i]}: {ejemplares[i]} Ejemplares')
                
        case 4:
            if not titulos:
                print('No hay titulos cargados.')
                continue
            
            busq_titulo = input('Que titulo desea consultar: ').strip().capitalize()
            if busq_titulo not in titulos:
                print('El titulo que busca no exite.')
            else:
                idx = titulos.index(busq_titulo)
                print(f'{busq_titulo} ejemplares: {ejemplares[idx]}')


        case 5:
            if not titulos:
                print('No hay titulos cargados.')
            
            print("Titulos Agostados.")
            i = 0
            while i < len(titulos):
                if ejemplares[i] == 0:
                    print(f"- {titulos[i]}")
                    
                i += 1
                if i == 0:
                    print('No hay titulos agotados.')
                    break
        case 6:
            
            titulo_new = input('Que titulo desea agregar: ').strip().capitalize()
            if titulo_new in titulos:
                print('El titulo ya existe.')
                continue
            elif titulo_new == " ":
                print('No puede agregar un titutlo vacio.')
            else:
                cant_ejemplares = input('Ingrese cantidad de ejemplares: ').strip()
                if not cant_ejemp.isdigit():
                    print('Debe ingresar un numero.')
                    break
                cantidad_int = int(cant_ejemp)
                if cantidad_int < 0:
                    print('La cantidad de ejemplares debe ser mayor a cero.')
                    break
                else: 
                    titulos.append(titulo_new)
                    ejemplares.append(cantidad_int)
            

        case 7:
            if not titulos:
                print('No hay titulos cargados.')
                continue
            
            busq_titulo = input('que titulo acualizar: ').strip().capitalize()
            if busq_titulo not in titulos:
                print('El titulo que busca no exite.')
                continue
            else:
                opcion = input('Para prestamo "R" para devolucion "D": ').strip().lower()
                if opcion == "r":
                    idx = titulos.index(busq_titulo)
                    if ejemplares[idx] == 0:
                        print('No hay ejemplares para prestar.')
                        continue
                    ejemplares[idx] -= 1
                    print('Ejemplares actializados.')
                elif opcion == "d":
                    idx = titulos.index(busq_titulo)
                    ejemplares[idx] += 1
                    print('Ejemplares actializados.')
                else:
                    print('Opcion invalida.')
                    continue
        case 0:
            seguir = False
            print('Hasta luego.')
        case _:
            print('ERROR, ingrese una opcion valida.')

