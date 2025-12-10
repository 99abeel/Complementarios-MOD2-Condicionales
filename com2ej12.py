print("--- Positivo o Negativo ---")
numero = float(input("Introduce un número: "))

# El enunciado pide considerar el 0 como positivo, por eso usamos >=
if numero >= 0:
    print("El número es POSITIVO.")
else:
    print("El número es NEGATIVO.")