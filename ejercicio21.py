# Escribe un programa que dada una hora determinada (horas y minutos), calcule los
# segundos que faltan para llegar a la medianoche.

print("Introduce la hora actual.")
horas = int(input("Horas (0-23): "))
minutos = int(input("Minutos (0-59): "))

# Comprobamos validez de los datos
if (0 <= horas <= 23) and (0 <= minutos <= 59):
    # Calculamos los segundos que han pasado desde el inicio del día
    segundos_transcurridos = (horas * 3600) + (minutos * 60)
    
    # Restamos del total de segundos de un día (86400)
    segundos_restantes = 86400 - segundos_transcurridos
    
    print(f"Faltan {segundos_restantes} segundos para la medianoche.")
else:
    print("La hora introducida no es válida.")