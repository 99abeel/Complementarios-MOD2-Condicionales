# Realiza un programa que diga si un número introducido por teclado es par y/o divisible entre 5.

numero = int(input("Introduce un número entero: "))

es_par = False
es_divisible_5 = False

# Comprobamos si es par
if numero % 2 == 0:
    es_par = True

# Comprobamos si es divisible entre 5
if numero % 5 == 0:
    es_divisible_5 = True

# Lógica de salida
if es_par and es_divisible_5:
    print("El número es PAR y DIVISIBLE entre 5.")
elif es_par:
    print("El número es PAR, pero NO es divisible entre 5.")
elif es_divisible_5:
    print("El número es IMPAR, pero es DIVISIBLE entre 5.")
else:
    print("El número no es ni par ni divisible entre 5.")