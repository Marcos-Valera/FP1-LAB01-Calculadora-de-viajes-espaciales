while True:
    distancia_km = int(input("Introduce la distancia en kilómetros >>> "))
    velocidad_kmh = int(input("Introduce la velocidad en kilómetros/hora >>> "))

    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24

    print(f"Tardarías {tiempo_dias} días en llegar.")

    quiere_seguir = input("¿Quieres hacer otra simulación (s/n) >>> ")

    while quiere_seguir not in "ns":
        quiere_seguir = input("Introduce una respuesta válida >>> ")

    if quiere_seguir == "n":
        break
        