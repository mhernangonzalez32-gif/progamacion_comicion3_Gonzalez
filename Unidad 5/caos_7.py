# Caso 1 — Biblioteca escolar — Préstamos de libros
# Requisitos: listas paralelas, menú con while, validaciones y manejo de casos borde.
# Sin diccionarios, sin clases, sin excepciones (solo controles con isdigit y lógica).

titulos = []        # lista de str
ejemplares = []     # lista de int (mismo índice que 'titulos')

seguir = True
while seguir:
    print("\n--- BIBLIOTECA ESCOLAR ---")
    print("1) Ingresar lista de títulos")
    print("2) Ingresar lista de ejemplares disponibles (por título)")
    print("3) Mostrar catálogo con stock")
    print("4) Consultar disponibilidad de un título")
    print("5) Listar títulos agotados (0 ejemplares)")
    print("6) Agregar título")
    print("7) Actualizar ejemplares (PRÉSTAMO / DEVOLUCIÓN)")
    print("0) Salir")

    op_txt = input("Elegí una opción: ").strip()
    if not op_txt.isdigit():
        print("⚠️ Opción inválida.")
        continue
    opcion = int(op_txt)

    if opcion == 1:
        # Ingresar lista de títulos (inicializa ejemplares en 0 para cada nuevo título)
        cant_txt = input("¿Cuántos títulos querés ingresar?: ").strip()
        if not cant_txt.isdigit():
            print("⚠️ Ingresá un entero válido.")
            continue
        n = int(cant_txt)
        if n < 0:
            print("⚠️ La cantidad debe ser ≥ 0.")
            continue

        cargados = 0
        while cargados < n:
            nombre = input(f"Título #{cargados+1}: ").strip()
            if nombre == "":
                print("⚠️ El título no puede estar vacío.")
                continue

            # evitar duplicados (case-insensitive)
            existe = False
            i = 0
            while i < len(titulos):
                if titulos[i].lower() == nombre.lower():
                    existe = True
                i += 1
            if existe:
                print("⚠️ Ese título ya existe.")
                continue

            titulos.append(nombre)
            ejemplares.append(0)  # por ahora 0; se ajusta con opción 2 o 7
            cargados += 1
            print("✅ Título agregado con ejemplares=0 (ajustá luego en opciones 2 o 7).")

    elif opcion == 2:
        # Ingresar lista de ejemplares para cada título existente (sin perder sincronía)
        if len(titulos) == 0:
            print("⚠️ No hay títulos cargados. Usá la opción 1 o 6 primero.")
            continue

        print("\nIngresá la cantidad para cada título (entero ≥ 0).")
        i = 0
        while i < len(titulos):
            ej_txt = input(f"'{titulos[i]}' ejemplares: ").strip()
            if not ej_txt.isdigit():
                print("⚠️ Entero inválido. Se mantiene el valor anterior.")
            else:
                cant = int(ej_txt)
                if cant < 0:
                    print("⚠️ Debe ser ≥ 0. Se mantiene el valor anterior.")
                else:
                    # Si la lista ejemplares tuviera menos items, los completamos
                    if i >= len(ejemplares):
                        ejemplares.append(cant)
                    else:
                        ejemplares[i] = cant
            i += 1
        # Si por alguna razón ejemplares quedó más largo, recortamos
        while len(ejemplares) > len(titulos):
            ejemplares.pop()
        print("✅ Actualización de ejemplares finalizada.")

    elif opcion == 3:
        # Mostrar catálogo con stock
        if len(titulos) == 0:
            print("No hay libros cargados.")
        else:
            print("\n--- CATÁLOGO ---")
            i = 0
            while i < len(titulos):
                print(f"{titulos[i]}: {ejemplares[i]} copias")
                i += 1

    elif opcion == 4:
        # Consultar disponibilidad de un título
        buscado = input("Título a consultar: ").strip()
        idx = -1
        i = 0
        while i < len(titulos):
            if titulos[i].lower() == buscado.lower():
                idx = i
            i += 1

        if idx == -1:
            print("⚠️ Título no encontrado.")
        else:
            print(f"Disponibles de '{titulos[idx]}': {ejemplares[idx]} copias")

    elif opcion == 5:
        # Listar títulos agotados
        print("\n--- TÍTULOS AGOTADOS (0) ---")
        hay = False
        i = 0
        while i < len(titulos):
            if ejemplares[i] == 0:
                print(f"- {titulos[i]}")
                hay = True
            i += 1
        if not hay:
            print("No hay títulos agotados.")

    elif opcion == 6:
        # Agregar un solo título con cantidad inicial
        nombre = input("Título nuevo: ").strip()
        if nombre == "":
            print("⚠️ El título no puede estar vacío.")
            continue

        existe = False
        i = 0
        while i < len(titulos):
            if titulos[i].lower() == nombre.lower():
                existe = True
            i += 1
        if existe:
            print("⚠️ Ese título ya existe.")
            continue

        ej_txt = input("Cantidad inicial de ejemplares (entero ≥ 0): ").strip()
        if not ej_txt.isdigit():
            print("⚠️ Ingresá un entero válido.")
            continue
        cant = int(ej_txt)
        if cant < 0:
            print("⚠️ Debe ser ≥ 0.")
            continue

        titulos.append(nombre)
        ejemplares.append(cant)
        print("✅ Título agregado al catálogo.")

    elif opcion == 7:
        # Actualizar ejemplares (préstamo o devolución)
        nombre = input("Título a actualizar: ").strip()
        idx = -1
        i = 0
        while i < len(titulos):
            if titulos[i].lower() == nombre.lower():
                idx = i
            i += 1

        if idx == -1:
            print("⚠️ Título no encontrado.")
            continue

        print("\n1) PRÉSTAMO (resta)")
        print("2) DEVOLUCIÓN (suma)")
        tipo_txt = input("Elegí 1 o 2: ").strip()
        if not tipo_txt.isdigit():
            print("⚠️ Opción inválida.")
            continue
        tipo = int(tipo_txt)

        cant_txt = input("Cantidad (entero ≥ 1): ").strip()
        if not cant_txt.isdigit():
            print("⚠️ Entero inválido.")
            continue
        cant = int(cant_txt)
        if cant < 1:
            print("⚠️ Debe ser ≥ 1.")
            continue

        if tipo == 1:
            # préstamo: no puede superar stock
            if cant > ejemplares[idx]:
                print("⚠️ No hay suficientes ejemplares disponibles para prestar.")
            else:
                ejemplares[idx] = ejemplares[idx] - cant
                print("✅ Préstamo registrado.")
        elif tipo == 2:
            ejemplares[idx] = ejemplares[idx] + cant
            print("✅ Devolución registrada.")
        else:
            print("⚠️ Opción inválida.")

    elif opcion == 0:
        seguir = False
        print("¡Chau! 👋")
    else:
        print("⚠️ Opción inválida.")

