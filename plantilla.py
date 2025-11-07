import csv
import os

CSV_FILE = "catalogo.csv"


# ----------------------------
# Utilidades (VALIDACIONES)
# ----------------------------

def normalizar_titulo(t: str) -> str:
    """
    Devuelve el título normalizado para comparación.
    Requisitos:
    - Quitar espacios sobrantes intermedios y extremos.
    - Pasar a minúsculas.
    TODO: implementar y devolver el string normalizado.
    """
    return t  # TODO


def titulo_valido(t: str) -> bool:
    """
    Un título es válido si, tras normalizar, no queda vacío.
    TODO: implementar y devolver True/False.
    """
    return False  # TODO


def pedir_titulo(msg: str) -> str:
    """
    Pide un título por input hasta que sea válido según las reglas del enunciado.
    Requisitos:
    - No vacío.
    - Comparación insensible a mayúsculas y con espacios normalizados.
    - Debe devolver el título ya normalizado para mostrar/guardar prolijo.
    TODO: implementar bucle de pedido y validación.
    """
    return ""  # TODO


def pedir_entero_no_negativo(msg: str) -> int:
    """
    Pide un entero >= 0 (usar validaciones simples como str.isdigit()).
    Debe volver a pedir si el valor no es válido.
    TODO: implementar bucle de pedido y validación; devolver int.
    """
    return 0  # TODO


# ----------------------------
# Persistencia CSV
# ----------------------------
def iniciar_archivo():
    if not os.path.exists('catalogo.csv'):
        with open('catalogo.csv', 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['titulo', 'cantidad'])
            escritor.writeheader()


def cargar_catalogo_desde_csv() -> list[dict]:
    lista = []
    try:
        with open('catalogo.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila['cantidad'] = int(fila['cantidad'])
                    lista.append({'titulo': fila['titulo'].capitalize(),'cantidad': fila['cantidad']})
                except ValueError:
                    print(f"Dato inválido")
    except FileNotFoundError:
        print('Archivo no encontrado.')

    return lista


def guardar_catalogo_a_csv(catalogo: list[dict]) -> None:
    with open('catalogo.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['titulo','cantidad'])
        escritor.writeheader()
        escritor.writerows(catalogo)
    


# ----------------------------
# Búsquedas y reglas de negocio
# ----------------------------

def buscar_indice_por_titulo(catalogo: list[dict], titulo_busqueda: str) -> int:
    """
    Devuelve el índice del libro cuyo título coincide (comparación normalizada).
    Si no existe, devuelve -1.
    TODO: implementar recorrido y comparación con normalización.
    """
    return -1  # TODO


def existe_titulo(catalogo: list[dict], titulo: str) -> bool:
    """
    True si el título ya existe en el catálogo (comparación normalizada).
    TODO: implementar usando buscar_indice_por_titulo.
    """
    return False  # TODO


# ----------------------------
# Operaciones (CRUD / reportes)
# ----------------------------

def ingresar_titulos_multiples(catalogo: list[dict]) -> list[dict]:
    try:
        cant_titulos = int(input("Cuantos titulos desea agregar?: "))
        for i in range(cant_titulos):
            nombre = input(f'Ingrese en nombre del titulo N {i+1}: ').lower().strip()
            catalogo.append({'titulo':nombre, 'cantidad':0})
        guardar_catalogo_a_csv(catalogo)
        print('Libro cargado.')
        return catalogo
    except ValueError:
        print('Ingrese un valor entero.')

def ingresar_ejemplares(catalogo: list[dict]) -> list[dict]:
    try:
        nombre = input(f'Titulo del libro  que desea agregar ejemplares: ').lower().strip()

        while True:
            cant = input('Cantidad de unidades: ')
            if cant.isdigit():
                cant = int(cant)
                break
            else:
                print('ingrese un valor valido')
            for fila in catalogo:
                if fila['titulo'].lower().strip() == nombre:
                    fila['cantidad'] += cant
                print(f"Se agregaron {cant} ejemplares de '{fila['titulo']}'.")
                guardar_catalogo_a_csv(catalogo)
                return catalogo
        catalogo.append({'titulo':nombre, 'cantidad':cant})
        guardar_catalogo_a_csv(catalogo)
        return 
    except ValueError:
        print('Debés ingresar un número entero.')

def mostrar_catalogo(catalogo: list[dict]) -> None:
    if not catalogo:
        print('No hay libros cargados.')
    else:
        for fila in catalogo:
            print(f"{fila['titulo']} - {fila['cantidad']} ejemplares")
            
    


def consultar_disponibilidad(catalogo: list[dict]) -> None:
    if not catalogo:
        print('No hay libros disponibles.')
        return
    for fila in catalogo:  
        nombre = input('Ingrese el titulo que quiere consultar: ').lower().strip()
        if fila in catalogo:
            if fila['titulo'].strip().lower() == nombre:
                cantidad = fila['cantidad']
                if cantidad > 0:
                    print(f"Hay {cantidad} ejemplares disponibles de '{fila['titulo']}'.")
            else:
                print(f"El titulo '{fila['titulo']}' esta cargado pero no tiene ejemplares disponibles.")
                break
        else:
            print("Titulo no disponible en el catalogo.")
    else:
        print('Titutlo no disponible.')


def listar_agotados(catalogo: list[dict]) -> None:
    if not catalogo:
        print("No hay libros en el catalogo.")
        return
    agotados = []
    for fila in catalogo:
        if fila['cantidad'] == 0:
            agotados.append(fila) 
    if not agotados:
        print("No hay titulos agotados.")
    else:
        print(" Titulos agotados:")
        for fila in agotados:
            print(f" - {fila['titulo'].capitalize()}")

def agregar_titulo(catalogo: list[dict]) -> list[dict]:
    """
    6) Agregar título individual (validar duplicados) con cantidad inicial.
    Requisitos:
    - TITULO válido y único.
    - CANTIDAD inicial >= 0.
    - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    TODO: implementar.
    """
    print("→ Agregar título: PENDIENTE DE IMPLEMENTAR")
    return catalogo  # TODO


def actualizar_ejemplares_prestamo_devolucion(catalogo: list[dict]) -> list[dict]:
    """
    7) Actualizar ejemplares:
        - Préstamo: restar 1 sólo si CANTIDAD > 0.
        - Devolución: sumar 1.
        - Guardar automáticamente tras cambios.
    Debe devolver el catálogo actualizado.
    TODO: implementar.
    """
    print("→ Préstamo/Devolución: PENDIENTE DE IMPLEMENTAR")
    return catalogo  # TODO


# ----------------------------
# Menú e interacción (sin globales)
# ----------------------------

def mostrar_menu() -> None:
    print("""
================= MENÚ BIBLIOTECA =================
1 - Ingresar títulos (múltiples)
2 - Ingresar ejemplares
3 - Mostrar catálogo
4 - Consultar disponibilidad
5 - Listar agotados
6 - Agregar título
7 - Actualizar ejemplares (Préstamo/Devolución)
8 - Salir
===================================================
""")


def main() -> None:
    print("📚 Iniciando sistema de Biblioteca…")
    catalogo: list[dict] = cargar_catalogo_desde_csv()
    if len(catalogo) == 0:
        print("ℹ️ Catálogo vacío o CSV no encontrado.")
        iniciar_archivo()
    else:
        print(f"✅ Catálogo cargado. {len(catalogo)} título(s).")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                catalogo = ingresar_titulos_multiples(catalogo)
            case "2":
                catalogo = ingresar_ejemplares(catalogo)
            case "3":
                mostrar_catalogo(catalogo)
            case "4":
                consultar_disponibilidad(catalogo)
            case "5":
                listar_agotados(catalogo)
            case "6":
                catalogo = agregar_titulo(catalogo)
            case "7":
                catalogo = actualizar_ejemplares_prestamo_devolucion(catalogo)
            case "8":
                print("👋 Saliendo. ¡Hasta luego!")
                break
            case _:
                print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
