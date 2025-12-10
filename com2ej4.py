print("--- EJERCICIO 4: Operaciones Básicas ---")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")

# Controlamos la división por cero para evitar errores
if num2 != 0:
    division = num1 / num2
    print(f"División: {division:.2f}")
else:
    print("División: No es posible dividir por cero.")