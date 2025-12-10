hora = int(input("Introduce la hora (0-23): "))

if 0 <= hora <= 23:
    if 6 <= hora <= 12:
        print("Buenos días")
    elif 13 <= hora <= 20:
        print("Buenas tardes")
    else:
        print("Buenas noches")
else:
    print("La hora introducida no es correcta.")