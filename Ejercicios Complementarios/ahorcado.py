import random

def elegir_band (x):
    return random.choice(x)
def iniciar_tablero(x):
    return ["_"] * len(bandas)
def mostrar_tablero(tablero):
    print("estado", " ".join(tablero))

bandas = ["Soda Stereo",
    "Patricio Rey y sus Redonditos de Ricota",
    "Divididos",
    "Los Fabulosos Cadillacs",
    "La Renga",
    "Charly García",
    "Gustavo Cerati",
    "Luis Alberto Spinetta",
    "Los Piojos",
    "Sumo"]

banda = elegir_band(bandas)
tablero = iniciar_tablero(bandas)

mostrar_tablero(tablero)

