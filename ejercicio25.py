# Diseña un algoritmo en el que se solicite un número por teclado y nos diga si es múltiplo de
# 2, de 3, de ambos o de ninguno. Por ejemplo, 6 es múltiplo de 2 y de 3; 4 es múltiplo de 2, 9
# es múltiplo de 3 y 5 no es múltiplo de ninguno.

# Solicitamos el número
numero = int(input("Introduce un número entero: "))

# Primero comprobamos si cumple ambas condiciones (divisible por 2 y por 3)
# Nota: Un número divisible por 2 y 3 es divisible por 6.
if numero % 2 == 0 and numero % 3 == 0:
    print(f"El número {numero} es múltiplo de 2 y de 3 (de ambos).")

# Si no es de ambos, miramos si es solo de 2
elif numero % 2 == 0:
    print(f"El número {numero} es múltiplo de 2.")

# Si no, miramos si es solo de 3
elif numero % 3 == 0:
    print(f"El número {numero} es múltiplo de 3.")

# Si no ha entrado en ninguno de los anteriores
else:
    print(f"El número {numero} no es múltiplo ni de 2 ni de 3.")