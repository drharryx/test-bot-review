import random

opciones = ["piedra", "papel", "tijeras"]

def jugar():
    puntaje_jugador = 0
    puntaje_computadora = 0
    
    while True:
        eleccion_jugador = input("Elige piedra, papel o tijeras (o 'q' para salir): ").lower()
        if eleccion_jugador == 'q':
            break
        
        if not eleccion_jugador in opciones:
            print("Opción inválida. Intenta de nuevo.")
            continue
        
        eleccion_computadora = random.choice(opciones)
        print("La computadora eligió: " + eleccion_computadora)
        
        if eleccion_jugador == eleccion_computadora:
            print("Empate!")
        elif eleccion_jugador == "piedra" and eleccion_computadora == "tijeras" or \
             eleccion_jugador == "papel" and eleccion_computadora == "piedra" or \
             eleccion_jugador == "tijeras" and eleccion_computadora == "papel":
            print("Ganaste!")
            puntaje_jugador = puntaje_jugador + 1
        else:
            print("Perdiste!")
            puntaje_computadora += 1
        
        print("Puntaje - Jugador: " + str(puntaje_jugador) + ", Computadora: " + str(puntaje_computadora))

    print("Puntaje final - Jugador: %d, Computadora: %d" % (puntaje_jugador, puntaje_computadora))
    if puntaje_jugador > puntaje_computadora:
        print("¡Felicidades, ganaste el juego!")
    elif puntaje_jugador < puntaje_computadora:
        print("Lo siento, perdiste el juego.")
    else:
        print("El juego terminó en empate.")

jugar()
