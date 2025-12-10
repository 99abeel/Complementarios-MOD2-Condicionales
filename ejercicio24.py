print("--- Calculadora de Tiempo de Cocción ---")
print("Opciones de carne: vacuno, cordero")
print("Opciones de punto: casi cruda, al punto, bien hecha")

# 1. Solicitamos datos de entrada
tipo_carne = input("Introduce el tipo de carne: ").lower()
modo_coccion = input("Introduce el punto de cocción: ").lower()
peso_usuario = float(input("Introduce el peso a cocinar (en gramos): "))

# Variables para almacenar los datos base según la selección
# Inicializamos en 0
tiempo_base_minutos = 0
peso_base_gramos = 0
datos_correctos = False

# 2. Lógica de selección
if tipo_carne == "vacuno":
    peso_base_gramos = 500
    if modo_coccion == "casi cruda":
        tiempo_base_minutos = 10
        datos_correctos = True
    elif modo_coccion == "al punto":
        tiempo_base_minutos = 17
        datos_correctos = True
    elif modo_coccion == "bien hecha":
        tiempo_base_minutos = 25
        datos_correctos = True

elif tipo_carne == "cordero":
    peso_base_gramos = 400
    if modo_coccion == "casi cruda":
        tiempo_base_minutos = 15
        datos_correctos = True
    elif modo_coccion == "al punto":
        tiempo_base_minutos = 25
        datos_correctos = True
    elif modo_coccion == "bien hecha":
        tiempo_base_minutos = 40
        datos_correctos = True

# 3. Cálculo y Salida
if datos_correctos:
    # Convertimos el tiempo base a segundos
    tiempo_base_segundos = tiempo_base_minutos * 60
    
    # Aplicamos la regla de proporcionalidad
    # (Peso Nuevo / Peso Base) * Tiempo Base
    tiempo_total_segundos = (peso_usuario / peso_base_gramos) * tiempo_base_segundos
    
    print("-" * 30)
    print(f"Para cocinar {peso_usuario}g de {tipo_carne} '{modo_coccion}':")
    print(f"El tiempo necesario es: {tiempo_total_segundos:.0f} segundos.")
else:
    print("Error: El tipo de carne o el modo de cocción no son válidos.")