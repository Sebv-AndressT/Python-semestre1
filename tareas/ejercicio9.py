numeros = [4,3,8,12,6,10,14,3,6]
print(numeros)

numeros.pop()
print(numeros)

numeros.insert(0, 2)
print(numeros)

print("la cantidad que se repite el numero 3 es:",numeros.index(3),"veces")
numeros.remove(3)
numeros.remove(3)
print(numeros)

print("la cantidad de elemntos en la lista son:",len(numeros))
print("y la suma en total de los numeros de la lista es:",sum(numeros),"y la media es de:",int(sum(numeros)/7))
numeros.sort()
print(numeros)
print("la mediana es:",numeros[3])