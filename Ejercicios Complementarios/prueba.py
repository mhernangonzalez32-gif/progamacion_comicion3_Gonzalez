import random

# ---------- Funciones de lógica ----------
def elegir_palabra(palabras):
    return random.choice(palabras)

def inicializar_tablero(palabra):
    return ["_"] * len(palabra)

def mostrar_tablero(tablero):
    print("Estado:", " ".join(tablero))

def intentar_letra(palabra, letra, tablero):
    """
    Actualiza el tablero con la letra si aparece en la palabra.
    Devuelve True si hubo al menos un acierto; False si no.
    """
    acierto = False
    for i in range(len(palabra)):
        if palabra[i] == letra and tablero[i] == "_":
            tablero[i] = letra
            acierto = True
    return acierto

def palabra_adivinada(tablero):
    return "_" not in tablero

def pedir_letra():
    """
    Pide al usuario una letra válida: longitud 1 y alfabética.
    Devuelve en minúscula.
    """
    while True:
        entrada = input("Ingresá una letra: ").strip().lower()
        if len(entrada) == 1 and entrada.isalpha():
            return entrada
        print("Entrada inválida. Debe ser UNA letra (a-z).")

# ---------- Juego ----------
def jugar_ahorcado():
    print("---- AHORCADO ----")
    palabras = ["python", "programa", "teclado", "depuracion", "variable", "funcion", "bucle", "lista", "arreglo"]
    palabra = elegir_palabra(palabras)            # string
    tablero = inicializar_tablero(palabra)        # lista de chars
    intentos = 6
    usadas = []                                   # lista de letras intentadas

    print("La palabra tiene", len(palabra), "letras.")
    mostrar_tablero(tablero)

    while intentos > 0 and not palabra_adivinada(tablero):
        letra = pedir_letra()

        # Ya intentada
        if letra in usadas:
            print("Ya probaste la letra:", letra, "(no se descuenta intento)")
            continue

        # Registrar intento
        usadas.append(letra)

        # Actualizar tablero
        if intentar_letra(palabra, letra, tablero):
            print("¡Bien! Adivinaste una letra.")
        else:
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")

        # Mostrar estado
        mostrar_tablero(tablero)
        print("Letras usadas:", ", ".join(usadas))

    # Fin del juego
    if palabra_adivinada(tablero):
        print("🎉 ¡Ganaste! La palabra era:", palabra)
    else:
        print("💀 Te quedaste sin intentos. La palabra era:", palabra)

# Punto de entrada
if __name__ == "__main__":
    jugar_ahorcado()