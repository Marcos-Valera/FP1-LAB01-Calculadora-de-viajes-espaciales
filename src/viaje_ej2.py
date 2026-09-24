distancia_km = int(input("Introduce la distancia en kilómetros >>> "))
velocidad_kmh = int(input("Introduce la velocidad en kilómetros/hora >>> "))

tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24

print(f"Tardarías {tiempo_dias} días en llegar.")