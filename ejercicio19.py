dia = input("Introduce un día de la semana: ").lower()

if dia == "lunes":
    print("El lunes a primera hora toca: Base de Datos")
elif dia == "martes":
    print("El martes a primera hora toca: Base de Datos")
elif dia == "miercoles" or dia == "miércoles":
    print("El miércoles a primera hora toca: Programación")
elif dia == "jueves":
    print("El jueves a primera hora toca: Sostenibilidad")
elif dia == "viernes":
    print("El viernes a primera hora toca: IPE")
elif dia == "sabado" or dia == "sábado" or dia == "domingo":
    print("¡Es fin de semana! No hay clase.")
else:
    print("Error: No has introducido un día válido.")