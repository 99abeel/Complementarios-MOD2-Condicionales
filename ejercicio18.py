
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