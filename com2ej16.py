print("--- EJERCICIO 16: Calificación Alfabética ---")
nota = float(input("Introduce la calificación numérica (0-10): "))

# Primero verificamos que la nota sea válida
if 0 <= nota <= 10:
    if 0 <= nota < 3:
        calificacion = "Muy Deficiente"
    elif 3 <= nota < 5:
        calificacion = "Insuficiente"
    elif 5 <= nota < 6:
        calificacion = "Bien"
    elif 6 <= nota < 9:
        calificacion = "Notable"
    else: # De 9 a 10
        calificacion = "Sobresaliente"
        
    print(f"Tu calificación es: {calificacion}")
else:
    print("Error: La nota debe estar entre 0 y 10.")