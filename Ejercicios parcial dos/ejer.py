import csv
import os



def iniciar_archivo():
    if not os.path.exists('especialidades.csv'):
        with open('especialidades.csv','w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['especialidades','cupos'])
            escritor.writeheader()

def cargar_datos():
    try:
        lista = []
        with open('especialidades.csv', 'r',encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo, fieldnames=['especialidades','cupos'])
            for fila in lector:
                try:
                    fila['cupos'] = int(fila['cupos'])
                    lista.append({'especialidades': fila['intrumento'].capitalize(), 'cupos':fila['cupos']})
                except ValueError:
                    print('Dato invalido en')
        return lista
    except FileExistsError:
        print('CSV incorrecto')

def actualizar_datos(lista):
    with open('especialidades.csv','w',newline='', encoding='Utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['especialidades','cupos'])
        escritor.writeheader()
        escritor.writerows(lista)

def mostrar_inventario(lista):
    if not lista:
        print('No hay especialidades cargadas.')
    else:
        for especialidad in lista:
            print(f'{especialidad['especialidades']} - {especialidad['cupos']} Cupos')

def especialidad_nueva(lista):
    try:
        cant_espe = int(input("Cuantas Especialidades desea agregar?: "))
        for i in range(cant_espe):
                nombre = (f'Ingrese en nombre de la especialidad N{i+1}')
                
    except ValueError:
        print('Ingrese un valor valido.')

def mostrar_menu():
    iniciar_archivo()

    print('--- MENU PRINCIPAL ---')
    print('1- Mostrar inventario.')
    print('2- Agregar instrumentos.')
    print('3- Editar unidades.')
    print('4- Eliminar instrumento.')
    print('5- Mostrar sin stock.')
    print('6- Vender / Comprar')
    print('7- Consultar stock.')
    print('8- Salir.')

def programa_principal():
    iniciar_archivo()
    mostrar_menu()
    lista = cargar_datos()
    opcion = int(input('Ingredes una opcion: '))
    while True:
        match opcion:
            case 1:
                mostrar_inventario(lista)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                print('Hasta luego.')
                break
            case _:
                print('Ingrese una opcion valida.')
if __name__ in '__main__':
    programa_principal()
