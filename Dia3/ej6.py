# Variables Globales
saldo = 1000
input_pin=1234
valor=0


# 1. Definir funciones
def verificar_pin(pin_usuario):
    # Tu código aquí (return True o False)
    if input_pin=="1234":
        return True
    else:
        return False
        

def retirar(monto):
    global saldo # Necesario para modificar la variable de afuera
    # Tu código aquí (if monto > saldo...)
   
     

# 2. Ejecución Principal
print("🏦 Bienvenido al Banco Python")
input_pin = input("Ingrese su PIN: ")
if verificar_pin(input_pin):
    print("Acceso concedido. Saldo actual:", saldo)
    
    try:
            while valor==0:
                monto_str = int(input("¿Cuánto desea retirar? "))
                if monto_str>saldo:
                    print ("fondos insuficientes")
                else:
                    print ("saldo retirado:",monto_str)
                    valor=1
        # Llamar a la función de retirar
        
    except ValueError:
        print("Error: Ingrese un número válido.")
else:
    print("PIN Incorrecto. Tofu en camino.")