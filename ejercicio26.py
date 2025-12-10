# Diseñe un algoritmo que lea un número de tres cifras y determine si es capicúa.

num = int(input("Introduce un número de tres cifras: "))

# Verificamos que sea de tres cifras
if 100 <= num <= 999:
    # Matemáticamente:
    # La cifra de las unidades es el resto de dividir entre 10
    unidades = num % 10
    
    # La cifra de las centenas es el resultado de la división entera entre 100
    centenas = num // 100
    
    if unidades == centenas:
        print(f"El número {num} ES capicúa.")
    else:
        print(f"El número {num} NO es capicúa.")
else:
    print("Error: El número introducido no tiene tres cifras.")