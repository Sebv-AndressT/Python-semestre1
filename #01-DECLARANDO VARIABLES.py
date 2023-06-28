#01-DECLARANDO VARIABLES
nombre = "Constanza"
name = "Sebastián"

PI = 3.14

#2-IMPRESION DE UNA VARIABLE
print(name)
print("hola soy",name)

#Declarando una tercera variable de tipo numerico
edad = 19 

#IMPRESION DE TEXTO + VARIABLE (IMPRESIÓN VARIABLE EDAD)
print("mi edad es de", edad) 

#04-IMPRIMIR 2 VARIABLES EN UNA MISMA LINEA (CONCATENACION CON SIGNO+,)

print("hola mi nombre es", nombre,"y tengo",edad) #impresion separando con comas 
print("hola mi nombre es"+" "+name+" "+"y tengo"+str(edad))
print(f"hola mi nombre es {nombre} y tengo {edad} años") #F-strings

#05-ACTUALIZANDO VARIABLES DE TIPO CADENA DE TEXTO
nombre = "Andres"
name = "Francisco"
print("hola mi nuevo nombre es", nombre) 
print("hola mi nuevo nombre es", name) 
#las variables pueden cambiar al sobreescribirlo

#06-no es recomendable usar variables en una sola linea

ciudad, region, pais, year = "puerto Montt", "los lagos", "chile", 2003
print("yo nací en", ciudad,"de la región de", region,"del pais de",pais,"en el año",year)

#introduccion del input
nombre1 = input("¿cual es tu nombre?\n")
edad1 = input ("¿cual es tu edad?\n")

print("tu nombre:",nombre1,"y tu edad es", edad1)