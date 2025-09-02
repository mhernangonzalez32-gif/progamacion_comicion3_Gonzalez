#Primer ejercico bucle for.

'''abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#corrimiento = int(input("Ingrese corrimiento"))
#abc.index(letra)
#(abc.index(letra) + corr) % 27

corrimiento = int(input("Ingrese corrimiento del encriptado: "))
for mensajes in range(1,5):
    
    palabra = input(f"Ingrese el mensaje N°{mensajes}: ").upper()
    msj_encriptado=""
    for letra in palabra:
        if letra in abc:
            posicion_original = abc.index(letra)
            nueva_posicion = (abc.index(letra) + corrimiento) % 27
            nueva_letra = abc[nueva_posicion]
            msj_encriptado += nueva_letra
        else:
            msj_encriptado += letra
    print(msj_encriptado)'''

#Segundo ejercicio bucle while.
import random
#opciones_num = ["1","2","3"]
opciones = ["piedra", "papel", "tijera"]
#eleccion = int(input("Elija una opcion.\n[1] Piedra\n[2] Papel\n[3] Piedra\n[4] Terminar juego\nEleccion: "))
eleccion = (0)
puntos_jugador = 0
puntos_pc = 0

while eleccion != 4:
    print("------------------------")
    eleccion = int(input("Elija una opcion.\n[1] Piedra\n[2] Papel\n[3] Tijeras\n[4] Terminar juego\n   Eleccion: "))
    if eleccion == 4:
        print("Fin del Juego Gracias!")
        print(f"---Contador---\n    Jugador: {puntos_jugador}\n    Pc: {puntos_pc}")
        break
    if eleccion < 1 or eleccion > 4:
        print("Ingrese una opcion valida")
        continue
    jugada_pc = random.choice(opciones)
    jugada_jugador = opciones[eleccion - 1]
    print(f"Tu eleccion: {jugada_jugador}\nLa pc eligio: {jugada_pc}")
    if jugada_jugador == jugada_pc:
        print("Es un empate")
    elif (jugada_jugador == "piedra" and jugada_pc == "tijera") or \
        (jugada_jugador == "tijera" and jugada_pc == "papel") or \
        (jugada_jugador == "papel" and jugada_pc == "piedra"):
        print("¡Ganaste!")
        puntos_jugador += 1
    else:
        print("Perdiste.")
        puntos_pc += 1
    

    print(f"---Contador---\n    Jugador: {puntos_jugador}\n    Pc: {puntos_pc}")
    print("------------------------")