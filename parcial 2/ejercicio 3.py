Set1 = {100, 250, 300, 1000}
Set2 = {150, 250, 500, 1000}

lista1 = list(Set1)
lista2 = list(Set2)

for e, n in zip(lista1, lista2):
    print(f"set 1: {e} | set 2: {n}")

print("el numero 100 solo esta presente en el 'set 1'")
print("el valor de 500 solo esta en el 'set 2' mientras que 700 no esta en ninguno")

num1 = int(100 * 100 * 100)
num2 = int(250 * 250 * 250)
num3 = int(300 * 300 * 300)
num4 = int(1000 * 1000 * 1000)
print(num2)

num5 = int(150 * 150 * 150)
num6 = int(250 * 250 * 250)
num7 = int(500 * 500 * 500)
num8 = int(1000 * 1000 * 1000)

sumas = [num1, num2, num3, num4]
sumass = [num5, num6, num7, num8]

union = set(sumas, sumass)
print(union)