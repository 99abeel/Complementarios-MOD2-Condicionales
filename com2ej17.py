print("\n--- EJERCICIO 17: Hora + 1 segundo ---")
h = int(input("Introduce las horas (0-23): "))
m = int(input("Introduce los minutos (0-59): "))
s = int(input("Introduce los segundos (0-59): "))

# Validamos la entrada básica
if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
    # Aumentamos un segundo
    s = s + 1
    
    # Comprobamos si los segundos desbordan (llegan a 60)
    if s == 60:
        s = 0
        m = m + 1
        
        # Comprobamos si los minutos desbordan
        if m == 60:
            m = 0
            h = h + 1
            
            # Comprobamos si las horas desbordan (pasan de 23 a 00)
            if h == 24:
                h = 0
                
    # Mostramos el resultado formateado con dos dígitos (ej. 09:05:01)
    # El :02d asegura que si es 5, se imprima "05"
    print(f"Hora + 1 segundo: {h:02d}:{m:02d}:{s:02d}")
    
else:
    print("Error: La hora introducida no es válida.")