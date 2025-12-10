print("--- EJERCICIO 6: Porcentaje de descuento ---")
precio_original = float(input("Precio original del artículo: "))
precio_venta = float(input("Precio de venta real: "))

descuento_euros = precio_original - precio_venta

if precio_original > 0:
    porcentaje = (descuento_euros / precio_original) * 100
    print(f"Se ha aplicado un {porcentaje:.2f}% de descuento.")
else:
    print("El precio original no puede ser 0.")