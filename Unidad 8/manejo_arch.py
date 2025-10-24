import os
def crear_archivo():
    if not os.path.exists("productos.txt"):
        with open("productos.txt", "w", encoding="UTF-8") as archivo:
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,300.0,15\n")
            archivo.write("Goma,80.0,50\n")
def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for fila in archivo:
            nombre, precio, cantidad = fila.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}.  ")
def agregar_producto():
    nombre = input("Nombre producto nuevo: ").strip().capitalize()
    precio = input("Precio del producto: ").strip()
    cantidad = input("Ingrese la cantiad: ").strip()
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
        print("Producto agregado correctamente.")
def cargar_productos():
    productos = []
    with open('productos.txt', 'r') as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {"nombre":nombre, "precio":precio, "cantidad":cantidad}
            productos.append(producto)
        return productos
    
def buscar_producto(productos):
    buscado = input("Ingrese el producto que busca: ").strip().lower()
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == buscado:
            print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")
    
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Archivo actualizado.")


'''1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad'''

'''2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30'''

'''3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.'''

'''4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.'''

'''5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.'''

'''6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.'''

while True:
    print('===MENU===')
    print("1) Mostrar producto.")
    print("2) Agregar producto.")
    print("3) Buscar producto.")
    print("0) Salir")
    opcion = int(input('Ingrese una opcion: '))

    match opcion:
        case 1:
            mostrar_productos()
        case 2:
            agregar_producto()
        case 3:
            productos = cargar_productos()
            buscar_producto(productos)
        case 0:
            print("Hasta luego.")
            break
        case _:
            print("Opcion ingresada invalida, ingrese nueva opcion.")


