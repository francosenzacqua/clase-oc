def es_par(numero):
    if(int(numero)%2 == 0):
        print ("el numero es par")
    else:
        print ("el numero es impar")
numero=int(input("Dime un numero:"))
print (es_par(numero))