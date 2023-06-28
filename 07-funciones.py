print("### 01 declarando la primera funcion ###")

def mi_primira_funcion():
    print("esta es mi primera funcion")

mi_primira_funcion()

print("### 02 declarando ###")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

### concatenar ###
print(concatenar(lista1, lista2))

print("### 03 funcion de multiplicacion pasando parametros ###")

def multiplicacion (num1,num2):
    return num1 * num2

print(multiplicacion(10,2))

print("### 04 ejemplo de una funcion ###")
    
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("ingrese un numero para a: "))
b = int(input("ingrese un segundo numero para b: "))

#se llama la funcion suma
resultado = suma(a, b)
print("el resultado es de la suma es de: ",resultado)

#se llama a la funcion resta
resultado2 = resta(a, b)
print("el resultado de la resta es de: ",resultado2)