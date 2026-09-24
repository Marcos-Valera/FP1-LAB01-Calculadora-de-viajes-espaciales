edad = int(input("Introduce tu edad >>> "))

if edad < 18:
    print("Debes ser mayor de edad.")
else:
    nivel_fisico = int(input("Introduce tu nivel físico (1-10) >>> "))
    if nivel_fisico < 5:
        print("Debes estar en mejor forma.")
    else:
        print("¡Listo para despegar!")