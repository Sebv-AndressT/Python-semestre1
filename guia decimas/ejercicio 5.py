def leer_numeros():
    numeros = []
    while True:
        numero = int(input("Ingrese un número positivo o -1 para finalizar:  "))
        if numero == -1:
            break
        elif numero > 0:
            numeros.append(numero)
    return numeros

def calcularmayor(numeros):
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

def calularsuma(numeros):
    sumatoria = 0
    for numero in numeros:
        sumatoria += numero
    return sumatoria

def calularsuma_pares(numeros):
    sumatoria_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            sumatoria_pares += numero
    return sumatoria_pares

def calularsuma_impares(numeros):
    sumatoria_impares = 0
    for numero in numeros:
        if numero % 2 != 0:
            sumatoria_impares += numero
    return sumatoria_impares

def calcular_promedio(numeros):
    sumatoria = calularsuma(numeros)
    cantidad = len(numeros)
    promedio = sumatoria / cantidad
    return promedio

numeros = leer_numeros()
mayor = calcularmayor(numeros)
sumatoria = calularsuma(numeros)
sumatoria_pares = calularsuma_pares(numeros)
sumatoria_impares = calularsuma_impares(numeros)
promedio = calcular_promedio(numeros)

print("El número mayor es:", mayor)
print("La sumatoria total es:", sumatoria)
print("La sumatoria de los números pares es:", sumatoria_pares)
print("La sumatoria de los números impares es:", sumatoria_impares)
print("El promedio es:", promedio)

if mayor > promedio:
    print(f"El número mayor es mayor que el promedio:{mayor}")
elif mayor < promedio:
    print(f"El número mayor es menor que el promedio: {mayor}")
else:
    print(f"El número mayor es igual que el promedio: {mayor}")




