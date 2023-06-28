#ejercicio 4

numero=int(input("ingrese un numero: "))
impar=(numero*(numero-1))+1
num=0
for i in range(numero):
    num= num + impar
    if i == (numero):
     break
    impar=impar+2
    print(impar)
print(f"el cubo de {numero} es: {num}")


