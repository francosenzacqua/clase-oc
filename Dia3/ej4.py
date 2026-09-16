# Tu código aquí 👇
def par(num1,num2,num3):
    if num1>num2 and num1>num3:
        print ("el numero mas grande es:",num1)
    elif num3>num2 and num3>num1:
        
        print ("el numero mas grande es:",num3)
    else:
        print ("el numero mas grande es:",num2)

nu1= int(input("Ingrese un numero:"))
nu2= int(input("Ingrese otro numero:"))
nu3= int(input("Ingrese otro numero:"))
    
par(nu1,nu2,nu3)