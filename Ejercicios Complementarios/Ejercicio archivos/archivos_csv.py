import csv
import os

def inicializar_archivo():
    if not os.path.exists('productos.csv'): 
        with open('productos.csv','w', encoding='UTF-8', newline='') as archivo:
            encabezado = ['nombre','precio']
            escritor = csv.DictWriter(archivo, fieldnames=encabezado)
            escritor.writeheader()

def cargar_productos():
    try:
        productos = []
        with open('productos.csv', 'r') as archivo:
            lector = csv.DictReader(archivo, fieldnames=['nombre','precio'])
            for fila in lector:
                try:
                    fila['precio'] = float(fila['precio'])
                    productos.append(fila)
                except ValueError:
                    pass
        return productos
    except FileNotFoundError:
        print('Archivo no encontrado')
def mostrar_productos():
    productos_mostrar = cargar_productos()
    total = 0 
    if not productos_mostrar:
        print('No hay productos para mostrar.')
    else:
        for prod in productos_mostrar:
            print(f"{prod['nombre']} - ${prod['precio']} ")
            total += prod['precio']
        print(f"El total acumulado de precios es ${total}")

def agregar_producto():
    try:
        while True:
            try:
                nombre = input('Ingrese el nombre del producto a agregar: ')
                if nombre == '':
                    print('El nombre no puede estar vacio. Y tiene que ser cadena.')
                    raise ValueError
                precio= float(input('Ingrese el precio del producto. '))
                print('Producto agregado correctamente.')
                with open('productos.csv', 'a', encoding='UTF-8', newline='') as archivo:
                    escritor = csv.DictWriter(archivo, fieldnames=['nombre','precio'])
                    escritor.writerow({'nombre':nombre, 'precio':precio})
                    break
            except ValueError:
                print('El valor del precio debe ser un numero')
                
    except FileNotFoundError:
        print('Archivo no encontrado.')
def eliminar_producto():
    productos_nuevos = []
    productos = cargar_productos()
    a_eliminar = input("Ingrese el producto que va a eliminar: ").strip().capitalize()
    for prod in productos:
        if a_eliminar != prod['nombre'].capitalize():
            productos_nuevos.append(prod)
        else:
            print("Producto eliminado.")
    try:
        with open('productos.csv', 'w', encoding='UTF-8', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['nombre','precio'])
            escritor.writeheader
            escritor.writerows(productos_nuevos)
    except FileExistsError:
        print('Archivo no encotrado')

def actualizar_precio():
    productos_nuevos = []
    productos = cargar_productos()
    a_actualizar = input('Ingrese producto a actualizar: ').strip().capitalize()
    for prod in productos:
        if a_actualizar == prod['nombre'].capitalize():
            while True:
                try:
                    precio_nuevo = float(input('ingrese el precio actualizado: '))
                    productos_nuevos.append({'nombre':prod['nombre'], 'precio':precio_nuevo})
                    break
                except ValueError:
                    print('El valor debe ser numerico.')
        else:
            productos_nuevos.append(prod)
        try:
            with open('productos.csv', 'w', encoding='UTF-8', newline='') as archivo: 
                escritor = csv.DictWriter(archivo, fieldnames=['nombre','precio'])
                escritor.writeheader()
                escritor.writerow(productos_nuevos)
        except FileNotFoundError:
            print('Archivo no encontrado.')
    print('actualizado')
#MAIN
def main():
    inicializar_archivo()
    print('1) Mostrar todos los productos registrados. ')
    print('2) Agregas un nuevo producto.')
    print('3) Eliminar un producto.')
    print('4) Salir del programa.')
    seguir = True
    while seguir:
        
        opcion = int(input('Ingrese una opcion: '))
        opc_int = int(opcion)
        match opc_int:
            case 1:
                mostrar_productos()
            case 2:
                agregar_producto()
            case 3:
                eliminar_producto()
            case 4:
                print('Hasta luego.')
                break

main()