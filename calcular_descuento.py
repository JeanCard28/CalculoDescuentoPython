def calcular_descuento(monto, porcentaje=13):
    descuento = monto * (porcentaje / 100)
    return descuento

# Solicitar al usuario que ingrese el monto de la compra
monto_compra = float(input("Ingrese el monto total de la compra: "))

descuento = calcular_descuento(monto_compra)
monto_final = monto_compra - descuento

# Mostrar resultados
print(f"Monto total: ${monto_compra:.2f}")
print(f"Descuento aplicado ({13}%): ${descuento:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")