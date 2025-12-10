# Escribe un programa que pida por teclado un día de la semana y que diga qué asignatura toca a
# primera hora ese día.

# Solicitamos el día y convertimos a minúsculas para evitar errores
dia = input("Introduce un día de la semana: ").lower()

if dia == "lunes":
    print("El lunes a primera hora toca: Matemáticas")
elif dia == "martes":
    print("El martes a primera hora toca: Física")
elif dia == "miercoles" or dia == "miércoles":
    print("El miércoles a primera hora toca: Historia")
elif dia == "jueves":
    print("El jueves a primera hora toca: Lengua")
elif dia == "viernes":
    print("El viernes a primera hora toca: Inglés")
elif dia == "sabado" or dia == "sábado" or dia == "domingo":
    print("¡Es fin de semana! No hay clase.")
else:
    print("Error: No has introducido un día válido.")