a = [10,9,12,15,18]
b = [21,8,15,3,12]

numeros = a
numeros1 = b
concatenar = numeros + numeros1
print(concatenar)

concatenar.insert(1, 30)
print(concatenar)

concatenar.sort()
print(concatenar)

c = [4,5,6]
numeros2 = c
concatenar1 = concatenar + numeros2
print(concatenar1)

print("la suma de todos los numeros es:",sum(concatenar))
print("la cantidad de numeros dentro de la lista es de:",len(concatenar1))
print("la media de la lista es de:",int(sum(concatenar1)/len(concatenar1)))
print("la mediana de la lista es",concatenar1[7])
