distancia_km = int(input("Introduce la distancia en kilómetros >>> "))

distancia_parada = 150000 # La distancia máxima que aguanta el combustible

paradas = (distancia_km - 1) // distancia_parada # El -1 es para obviar paradas exactamente en el destino450

for parada in range(1, paradas + 1):
    print(f"Parada en el km {parada * distancia_parada}")

if paradas == 0:
    print("No hace falta parar, el combustible llega hasta el final")