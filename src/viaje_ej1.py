distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")

# El primer cambio ha sido que, en lugar de obtener la solución completa, ha obtenido la parte entera de los días.

# El segundo cambio ha sido que, al convertir también el tiempo en horas a una parte entera (tipo int), la división de ambos números
# enteros ha hecho que no se vean los decimales, cuando antes, al dividir de forma normal, da la solución en tipo float.