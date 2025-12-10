# Escribe un programa que calcule el salario neto semanal de un trabajador en función del
# número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
# • Las primeras 35 horas se pagan a tarifa normal.
# • Las horas que pasen de 35 se pagan a 1,5 veces la tarifa normal.
# • Las tasas de impuestos son:
# • Los primeros 500 euros son libres de impuestos.
# • Los siguientes 400 tienen un 25% de impuestos.
# • Los restantes un 45% de impuestos.
# Escribir nombre, salario bruto, tasas y salario neto.

nombre = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas esta semana: "))
tarifa = float(input("Tarifa por hora ordinaria (€): "))


salario_bruto = 0.0

if horas <= 35:
    salario_bruto = horas * tarifa
else:
    horas_extra = horas - 35
    salario_bruto = (35 * tarifa) + (horas_extra * tarifa * 1.5)

impuestos = 0.0

if salario_bruto <= 500:
    impuestos = 0.0
elif salario_bruto <= 900:
    base_imponible = salario_bruto - 500
    impuestos = base_imponible * 0.25
else:
    impuesto_tramo_2 = 400 * 0.25 
    base_tramo_3 = salario_bruto - 900
    impuesto_tramo_3 = base_tramo_3 * 0.45
    
    impuestos = impuesto_tramo_2 + impuesto_tramo_3

salario_neto = salario_bruto - impuestos

print("-" * 30)
print(f"Nómina de: {nombre}")
print(f"Salario Bruto: {salario_bruto:.2f} €")
print(f"Tasas (Impuestos): {impuestos:.2f} €")
print(f"Salario Neto: {salario_neto:.2f} €")
print("-" * 30)