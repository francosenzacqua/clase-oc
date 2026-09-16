# Tu código aquí 👇
precio = input("¿Cual es el precio original? ")
prec = float(precio)  
descuento = input("¿Que porcentaje de descuento? ")
desc = int(descuento)
Resultado = prec-desc/100*prec
print("Monto a pagar:", Resultado)