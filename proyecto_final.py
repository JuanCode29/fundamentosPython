import random

opciones_jugadas = ["piedra", "papel", "tijera"]
jugadores = []
round = 1
print("BIENVENIDOS AL JUEGO: PIEDRA, PAPEL O TIJERA\n")
print("Ingresar nombres de Jugadores")

for num_jugador in range(1, 3):
    nombre_jugador = input(f"Jugador {num_jugador}: ")
    jugadores.append(nombre_jugador)

print("Jugadores registrados:", jugadores)

puntajes = {
  jugadores[0]: 0, 
  jugadores[1]: 0
}

while True:
    print(f"\n--- Ronda {round}---")
    round = round + 1
    jugador_inicial = random.choice(jugadores)
    otro_jugador = jugadores[1] if jugador_inicial == jugadores[0] else jugadores[0]

    print(f"{jugador_inicial} inicia la ronda.")
    jugada1 = input(f"{jugador_inicial}, selecciona tu jugada: {', '.join(opciones_jugadas)}: ").lower()

    while jugada1 not in opciones_jugadas:
        print("Jugada inválida. Selecciona entre:", ', '.join(opciones_jugadas))
        jugada1 = input().lower()

    jugada2 = input(f"{otro_jugador}, selecciona tu jugada: {', '.join(opciones_jugadas)}: ").lower()

    while jugada2 not in opciones_jugadas:
        print("Jugada inválida. Selecciona entre:", ', '.join(opciones_jugadas))
        jugada2 = input().lower()

    print(f"{jugador_inicial}: {jugada1}\n{otro_jugador}: {jugada2}")

    if jugada1 == jugada2:
        print("Empate en esta ronda.")
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "papel" and jugada2 == "piedra") or \
         (jugada1 == "tijera" and jugada2 == "papel"):
        print(f"{jugador_inicial} gana esta ronda.")
        puntajes[jugador_inicial] += 1
    else:
        print(f"{otro_jugador} gana esta ronda.")
        puntajes[otro_jugador] += 1

    if puntajes[jugadores[0]] >= 2 or puntajes[jugadores[1]] >= 2:
        break

print("\n--- Resultado Final ---")
ganador = max(puntajes, key=puntajes.get)
print(f"{jugadores[0]}: {puntajes[jugadores[0]]} puntos")
print(f"{jugadores[1]}: {puntajes[jugadores[1]]} puntos")
print(f"Ganador de la partida: {ganador}")

