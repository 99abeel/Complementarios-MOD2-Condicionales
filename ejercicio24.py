# El tiempo de cocción. 
# Sabiendo que: 
# ● Para cocinar 500 gramos de carne de vacuno, se necesita: 
# ○ 10 minutos si quieres una cocción casi cruda 
# ○ 17 minutos si quieres una cocción al punto 
# ○ 25 minutos si quieres una cocción bien hecha. 
# ● Para cocinar 400 gramos de carne de cordero se necesita: 
# ○ 15 minutos si quieres una cocción casi cruda 
# ○ 25 minutos si quieres una cocción al punto 
# ○ 40 minutos si quieres una cocción bien hecha. 
# ● El tiempo de cocción es proporcional al peso. 
# Dependiendo de la información introducida por el usuario (tipo de carne, modo de cocción y 
# peso), mostrar el tiempo de cocción de una carne en segundos. 

vacuno1 = 10
vacuno2= 17
vacuno3 = 25

cordero1 = 15
cordero2 = 25
cordero3= 40
print("--- Tipos de carne --- ")
print("1. Vacuno.")
print("2. Cordero.")

carne = input("Introduce tipo de carne: ")

match carne:
    case '1': carne='vacuno'
    case '2': carne='cordero'
    case _: print("Eleccion de tipo de carne incorrecta.")

print("--- tipo de cocción ---")
print("1. Casi cruda.")
print("2. Al punto.")
print("3. Bien hecha.")

punto=int(input("Introduce modo de cocción: (1, 2 o 3): "))
if punto<1 or punto>3:
    print("Error, de punto de cocción.")
else:
    try:
        peso = int(input("Introduce el peso de la carne: "))
        peso=abs(peso)
    except ValueError:
        print("El peso debe ser numerico.")
    else:

        tiempo=0
        if carne == 'vacuno':
            match punto:
                case 1: tiempo=(vacuno1*peso)/500
                case 2: tiempo=(vacuno2*peso)/500
                case 3: tiempo=(vacuno3*peso)/500
                case _: print("Opcion no valida.")

        elif(carne == 'cordero'):
            match punto:
                case 1: tiempo=(cordero1*peso)/400
                case 2: tiempo=(cordero2*peso)/400
                case 3: tiempo=(cordero3*peso)/400
                case _: print("Opcion no valida.")  

        print(f"Se necesita cocer durante {tiempo} minutos.")
        print(f"Se necesita cocer durante", tiempo*60, "segundos")