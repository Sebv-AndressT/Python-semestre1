n1 = int(input("introduzca el primer numero"))
n2 = int(input("introduzca el segundo numero"))
n3 = int(input("introduzca el tercer numero"))
if n1 > n2 and n2 > n3 :
    print(n1," es el mayor, le sigue ",n2,"y el menor es ",n3)

if n2<n1 and n1<n3 :
    print(n3," es el mayor, le sigue ",n1,"y el menor es ",n2)

if n3<n1 and n2>n1 :
    print(n2," es el mayor, le sigue ",n1," y el mayor es ",n3)