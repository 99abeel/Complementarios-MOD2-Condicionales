# Realiza un programa que pida una hora por teclado y que muestre luego buenos días,
# buenas tardes o buenas noches según la hora. Se utilizarán los tramos de 6 a 12, de 13 a 20 y de
# 21 a 5. respectivamente. Sólo se tienen en cuenta las horas, los minutos no se deben introducir por
# teclado

# Solicitamos la hora (sin minutos)
hora = int(input("Introduce la hora (0-23): "))

# Validamos que la hora sea correcta
if 0 <= hora <= 23:
    if 6 <= hora <= 12:
        print("Buenos días")
    elif 13 <= hora <= 20:
        print("Buenas tardes")
    else:
        # Esto cubre de 21 a 23 y de 0 a 5
        print("Buenas noches")
else:
    print("La hora introducida no es correcta.")