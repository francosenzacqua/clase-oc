def calcular_precio_final(precio, descuento):
    descuento_aplicado = precio * descuento / 100
    precio_final = precio - descuento_aplicado
nom=int(input("ingresa el precio: "))
no=int(input("ingresa el porcentaje de descuento: "))
print("precio final es: ", precio_final)