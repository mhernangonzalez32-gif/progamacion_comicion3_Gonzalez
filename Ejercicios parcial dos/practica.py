import os  

import csv


def inicializar_archivo():
    if not os.path.exists("texto.csv"):
        with open('texto.csv','w',newline='', encoding='utf-8') as archivo:
            campos = ['instrumento','cantidades']
            escritor = csv.DictWriter(archivo,fieldnames=campos)
            escritor.writeheader()
            
def cargar_datos():
    lista = []
    try:
        with open("texto.csv", "r", encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo,fieldnames=['instrumento','cantidades'])
            next(lector)
            for i in lector:
                try:
                    i["cantidades"] = int(i["cantidades"])
                    lista.append(i)

                except ValueError:
                    print("Dato invalido")

    except FileExistsError:
        print('No existe el archivo csv')