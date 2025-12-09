print("Introduce la hora actual.")
horas = int(input("Horas (0-23): "))
minutos = int(input("Minutos (0-59): "))

if (0 <= horas <= 23) and (0 <= minutos <= 59):
    segundos_transcurridos = (horas * 3600) + (minutos * 60)
    
    segundos_restantes = 86400 - segundos_transcurridos
    
    print(f"Faltan {segundos_restantes} segundos para la medianoche.")
else:
    print("La hora introducida no es válida.")