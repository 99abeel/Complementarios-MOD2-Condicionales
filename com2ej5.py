import math

print("--- EJERCICIO 5: Geometría circular ---")
radio = float(input("Introduce la longitud del radio: "))

# Fórmulas
longitud = 2 * math.pi * radio
area = math.pi * (radio ** 2)
volumen = (4/3) * math.pi * (radio ** 3)

print(f"Longitud de la circunferencia: {longitud:.2f}")
print(f"Área del círculo: {area:.2f}")
print(f"Volumen de la esfera: {volumen:.2f}")