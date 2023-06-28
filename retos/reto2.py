

estuduante = input("¿cual es el nombre del estudiante?")
asignatura = input("¿cual es la asgnatura del estudiante?")
lab1 = float(input ("¿cual es la nota del primer laboratorio?"))
lab2 = float(input ("¿cual es la nota del segundo laboratorio?"))
promedio = float((lab1*0.3)+(lab2*0.7))

notas = {
    "estudiante": estuduante,
    "asignatura": asignatura,
    "nota de lab n1": lab1,
    "nota de lab n2": lab2,
    "promedio de notas":round (promedio, 1)
}

print(notas)