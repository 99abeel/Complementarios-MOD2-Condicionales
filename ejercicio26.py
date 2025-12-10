num = int(input("Introduce un número de tres cifras: "))

if 100 <= num <= 999:
    unidades = num % 10
    
    centenas = num // 100
    
    if unidades == centenas:
        print(f"El número {num} ES capicúa.")
    else:
        print(f"El número {num} NO es capicúa.")
else:
    print("Error: El número introducido no tiene tres cifras.")