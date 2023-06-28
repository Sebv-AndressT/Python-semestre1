a = 4
b =5
print("suma entre a+ b es:",a + b)

t = 5.39
g = 9.81

v = g*t

print(f"la velocidad del objeto en caida libre es de: {v} n/s")
print("la velocidad del objeto en caida libre es de: {:2}")

#variable compleja
c2 = complex(3, -5)
print(" el numero complejo es:",c2)
print(c2.real)
print(c2,)

#operadores de comparacion 
print(a == b)# es igual
print(a != b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#comparando cadena de caracteres
animal_domestico = "gato"
animal_salvaje = "leopardo"
print(animal_domestico = animal_salvaje)
print(animal_salvaje != animal_domestico)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)

#operadores logicos
bencina = True
encendido = True
edad = 19

#poerador "and"
if bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

#operador "or"
if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

#operador "not" junto al "and"
if not bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede avanzar ")

#operador "not" con "and" y "or"   
if not bencina or (encendido and edad >= 18):
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede avanzar")
    
    