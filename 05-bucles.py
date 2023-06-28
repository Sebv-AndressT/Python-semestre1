edad = 15
num = 0
#bucle infinito
#while edad < 18:
#    print("eres menor de edad, no puedes manejar")

#bucle infinto
#while True:
#   print(num)
#   num += 2
#num = num+2

while num <= 100:
    print(num)
    num += 2
print("primer bucle terminado")

while num <= 200:
    print(num)
    num += 2
else:
    print("mi condicion supero 200")
print("segundo bucle terminado")

while num <= 300:
    print(num)
    num +=2
    if num == 250: #el if siempre tiene que estar dentro del bucle 
        print("mi condicion es igual a 250")
print("tercer bucle terminado")

while num <= 400:
    print(num)
    num += 2
    if num == 350:
        print("se detiene la ejecucion del bucle")
        break
print(num)
print("cuarto bucle terminado")

#loop infinito
"""while True:
    parametro = input("<")
    if parametro == "exit":
        break
    else:
        print(parametro)"""

#impresion de una lista 
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

#for 2
newlist = [1,2,3,4,5,6,7,8,9,10]
for i in newlist:
    print(i)

#for 3
for i in range(11):
    print(i)
    
