edad = int(input("Introduce tu edad >>> "))

while edad < 1 or edad > 99:
    edad = int(input("Debes de introducir una edad entre 1 y 99 >>> "))
if edad < 18:
    print("Debes ser mayor de edad.")
else:
    nivel_fisico = int(input("Introduce tu nivel físico (1-10) >>> "))

    while nivel_fisico < 0 or nivel_fisico > 10:
        nivel_fisico = int(input("Debes introducir un número entre 1 y 10 >>> "))

    if nivel_fisico < 5:
        print("Debes estar en mejor forma.")
    else:
        print("¡Listo para despegar!")