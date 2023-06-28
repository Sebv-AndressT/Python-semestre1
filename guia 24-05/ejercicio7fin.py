#ejercicio 7 factoriales

num=int(input("ingrese un numero: "))
factorial=1
if num!=0:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial:",factorial)