print("--- Ejercicio 1 ---")
for i in range(1, 21):
    print(i, end=" ")
print() # Salto de línea al final

print("\n--- Ejercicio 2 ---")
# Empezamos en 2, llegamos hasta 201 (para incluir el 200), salto de 2
for i in range(2, 201, 2):
    print(i, end=" ")
print()

print("\n--- Ejercicio 3 ---")
for i in range(1, 201):
    # Comprobamos si es par con el módulo
    if i % 2 == 0:
        print(i, end=" ")
print()

print("\n--- Ejercicio 4 ---")
n = int(input("Introduce un número N: "))

for i in range(1, n + 1):
    print(i, end=" ")
print()

print("\n--- Ejercicio 5: Factorial ---")
n = int(input("Introduce número para calcular factorial: "))
factorial = 1

# Si introduce 0, el bucle no se ejecuta y queda en 1 (que es correcto)
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")

print("\n--- Ejercicio 6: Detección de negativos ---")
hay_negativo = False

print("Introduce 100 números:")
for i in range(100):
    num = int(input(f"Número {i+1}: "))
    if num < 0:
        hay_negativo = True

if hay_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se han introducido números negativos.")

print("\n--- Ejercicio 7: Contadores ---")
positivos = 0
negativos = 0

for i in range(100):
    num = int(input(f"Número {i+1}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

print("\n--- Ejercicio 8: Secuencia hasta el 0 ---")
positivos = 0
negativos = 0
hay_negativo = False

num = int(input("Introduce un número (0 para salir): "))

while num != 0:
    if num > 0:
        positivos += 1
    else: # Si no es 0 (condicion del while) y no es positivo, es negativo
        negativos += 1
        hay_negativo = True
    
    # Leemos el siguiente número
    num = int(input("Introduce un número (0 para salir): "))

print(f"Total Positivos: {positivos}")
print(f"Total Negativos: {negativos}")
if hay_negativo:
    print("Sí se ha introducido algún número negativo.")
else:
    print("No hubo números negativos.")

print("\n--- Ejercicio 9: Suma y Producto ---")
suma = 0
producto = 1

for i in range(1, 11):
    suma += i
    producto *= i

print(f"La suma es: {suma}")
print(f"El producto es: {producto}")

print("\n--- Ejercicio 10: Buscar el 10 ---")
hubo_diez = False

nota = int(input("Introduce nota (-1 para terminar): "))

while nota != -1:
    if nota == 10:
        hubo_diez = True
    
    nota = int(input("Introduce nota (-1 para terminar): "))

if hubo_diez:
    print("SÍ hubo alguna nota con valor 10.")
else:
    print("NO hubo ninguna nota con valor 10.")

print("\n--- Ejercicio 11: Sumas separadas ---")
suma_pares = 0
suma_impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")

print("\n--- Ejercicio 12: Potencia manual ---")
base = int(input("Introduce la base (A): "))
exponente = int(input("Introduce el exponente (B): "))

resultado = 1

# Multiplicamos la base por sí misma tantas veces como diga el exponente
for i in range(exponente):
    resultado = resultado * base

print(f"{base} elevado a {exponente} es: {resultado}")

print("\n--- Ejercicio 13: El ordenador adivina ---")
print("Piensa un número del 1 al 100.")
input("Pulsa Enter cuando estés listo...")

minimo = 1
maximo = 100
respuesta = "" # Inicializamos vacía para entrar al bucle

while respuesta != "igual":
    # El ordenador propone el número central del rango
    intento = (minimo + maximo) // 2
    
    print(f"¿Es el {intento}?")
    print("Escribe: 'mayor' (si tu numero es mayor), 'menor' (si es menor) o 'igual'")
    respuesta = input().lower()
    
    if respuesta == "mayor":
        # Si tu número es mayor, el mínimo sube
        minimo = intento + 1
    elif respuesta == "menor":
        # Si tu número es menor, el máximo baja
        maximo = intento - 1
        
print(f"¡He acertado! El número era {intento}.")

print("\n--- Ejercicio 14: Desglose de billetes ---")
cantidad = int(input("Introduce la cantidad en euros (múltiplo de 5): "))

if cantidad % 5 == 0:
    # Lista con los tipos de billetes
    billetes = [500, 200, 100, 50, 20, 10, 5]
    
    print(f"Para {cantidad} € se necesitan:")
    
    for billete in billetes:
        # División entera para saber cuántos billetes de este tipo caben
        num_billetes = cantidad // billete
        
        if num_billetes > 0:
            print(f"{num_billetes} billete(s) de {billete} €")
            
            # Actualizamos la cantidad pendiente usando el módulo (resto)
            cantidad = cantidad % billete
else:
    print("Error: La cantidad debe ser múltiplo de 5.")

