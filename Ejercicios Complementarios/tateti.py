
# Hernán aprendiendo listas 💪

# Creamos el tablero con 9 posiciones
celdas = [str(i) for i in range(1, 10)]

jugador = "X"
ganador = False

print("===== TA-TE-TI =====")

# Mostramos el tablero inicial
print(f" {celdas[0]} | {celdas[1]} | {celdas[2]} ")
print("---+---+---")
print(f" {celdas[3]} | {celdas[4]} | {celdas[5]} ")
print("---+---+---")
print(f" {celdas[6]} | {celdas[7]} | {celdas[8]} ")

# Bucle principal
while True:
    # Pedimos jugada
    pos = int(input(f"Jugador {jugador} - elegí una posición (1-9): "))
    while pos < 1 or pos > 9 or celdas[pos-1] in ("X", "O"):
        print("→ Posición inválida o casilla ocupada.")
        pos = int(input(f"Jugador {jugador} - elegí una posición (1-9): "))
    
    # Colocamos la jugada en el tablero
    celdas[pos-1] = jugador

    # Mostramos el tablero actualizado
    print(f" {celdas[0]} | {celdas[1]} | {celdas[2]} ")
    print("---+---+---")
    print(f" {celdas[3]} | {celdas[4]} | {celdas[5]} ")
    print("---+---+---")
    print(f" {celdas[6]} | {celdas[7]} | {celdas[8]} ")

    # Revisamos si el jugador ganó
    lineas = [
        (0,1,2), (3,4,5), (6,7,8),  # filas
        (0,3,6), (1,4,7), (2,5,8),  # columnas
        (0,4,8), (2,4,6)            # diagonales
    ]
    for a, b, c in lineas:
        if celdas[a] == celdas[b] == celdas[c] == jugador:
            print(f"🎉 ¡Ganó {jugador}!")
            ganador = True
            break

    if ganador:
        break

    # Revisamos empate (todas ocupadas)
    if all(x in ("X","O") for x in celdas):
        print("🤝 ¡Empate!")
        break

    # Cambiamos de jugador
    jugador = "O" if jugador == "X" else "X"