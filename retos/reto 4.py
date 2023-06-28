a = int(input("ingresar numero numero: "))

if a % 2 == 0:
    print(a, "es un numero par")
else:
    print(a, "el numero es impar")

def primo(a):
    if a < 2:
        return False
    for i in range(2,int(a/2) + 1):
        if (a%i) == 0:
            return False
        return True
    
if primo(a):
    print(a,"no es un numero primo")
else:
    print(a,"es un numero primo")

if a < 50:
    print(a,"el numero es menor a 50")
elif a == 50:
    print(a,"el numero es igual a 50")
else:
    print(a,"es mayor a 50")





