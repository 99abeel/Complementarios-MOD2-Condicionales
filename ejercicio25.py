numero = int(input("Introduce un número entero: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"El número {numero} es múltiplo de 2 y de 3 (de ambos).")

elif numero % 2 == 0:
    print(f"El número {numero} es múltiplo de 2.")

elif numero % 3 == 0:
    print(f"El número {numero} es múltiplo de 3.")

else:
    print(f"El número {numero} no es múltiplo ni de 2 ni de 3.")