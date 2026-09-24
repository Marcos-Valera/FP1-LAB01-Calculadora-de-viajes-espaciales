distancia_km = 225000000 # Distancia Tierra-Marte
velocidad_kmh = 10000 # Valor inicial
saltos = 10000 # Saltos de 10.000 km/h en 10.000 km/h
velocidad_tope = 50000 # La velocidad hasta la que se llega

for velocidad in range(velocidad_kmh, velocidad_tope + 1, saltos):
    tiempo_horas = distancia_km / velocidad
    tiempo_dias = tiempo_horas / 24
    tiempo_semanas = tiempo_dias // 7
    dias_restante = tiempo_dias - tiempo_semanas * 7
    print(f"Velocidad: {velocidad} km/h  →  Tiempo: {tiempo_semanas} semanas y {dias_restante} días")
