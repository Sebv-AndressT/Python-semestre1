import random

numeros = [random.randint(40, 350) for x in range(20)]
newlist = list(numeros)
print(newlist)
print(f"la cantidad de numeros en la lista es de:{len(newlist)}")
num = int(input("ingrese un numero del 0 al 19 para buscar un numero de la lista: "))
print(newlist[num])
print(f"el numero en la posicion seleccionada se repite: {newlist.count(num)} veces")