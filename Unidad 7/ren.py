def procesar_frase():
    frase = input("Ingresa una frase o un texto: ")
    palabras = frase.lower().split()
    palabras_limpias = []
    puntuacion = ".,:;!?"
    for palabra in palabras:
        palabra_limpia = palabra.strip(puntuacion)
        if palabra_limpia: # Aseguramos no agregar strings vacíos
            palabras_limpias.append(palabra_limpia)
    palabras_unicas = set(palabras_limpias)
    print("\n------------------------------")
    print(f"Palabras únicas (Set): {palabras_unicas}")
    print("------------------------------")
    conteo_palabras = {}
    for palabra in palabras_limpias:
        conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
    print("Conteo de cada palabra (Diccionario):")
    for palabra, conteo in conteo_palabras.items():
        print(f"'{palabra}': {conteo}")
    print("------------------------------")
procesar_frase()