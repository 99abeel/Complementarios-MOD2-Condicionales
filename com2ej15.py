print("--- Mayor de tres números ---")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

# Lógica algorítmica clásica
if n1 > n2 and n1 > n3:
    print(f"El mayor es el primero: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"El mayor es el segundo: {n2}")
else:
    print(f"El mayor es el tercero: {n3}")

# Nota: En Python real también podrías usar simplemente: print(max(n1, n2, n3))