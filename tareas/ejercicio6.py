grupo1 = {"Marcos","Gabriela","Benjamin","Matias"}
grupo2 = {"Marcos","Nicolas","Diego","Matias"}

print(type(grupo1))
print(type(grupo2))

repetidos = grupo1.intersection(grupo2)

if len(repetidos)>0:
    print("los estudiantes que estan repetidos son :",repetidos)
    for estudiantes in repetidos:
        print(estudiantes)
else: 
    print("no hay estudiantes repetidos")