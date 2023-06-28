import random
def pares(numeros):
    numeros_pares = []

    for n in numeros:
        if n % 2 == 0:
            numeros_pares.append(n)

    return numeros_pares

def impares(numeros):
    numeros_impares = []

    for i in numeros:
        if i % 2 == 1:
            numeros_impares.append(i)

    return numeros_impares

num = int(input("ingrese una cantidad de numeros aleatorio: "))
numeros = [random.randint(0, 100) for x in range(num)]
resultado = pares(numeros)
resultado2 = impares(numeros)
suma = sum(numeros)

print("lista con cantidad de numeros:",numeros)
print("numeros pares:",resultado)
print("numeros impares",resultado2)
print("la suma total de los numeros es de:",suma)
