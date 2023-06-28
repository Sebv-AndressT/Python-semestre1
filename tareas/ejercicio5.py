nombre = input("¿nombre del estudiante?")

lab1 = float(input("ingrese la nota del laboratorio 1 "))
lab2 = float(input("ingrese la nota del laboratorio 2 "))
lab3 = float(input("ingrese la nota del laboratorio 3 "))

promedio = lab1*0.3 + lab2*0.4 + lab3*0.3

notas = {
    "estudiante": nombre,
    "asignatura": "Programacion",
    "nota del laboratorio 1": lab1,
    "nota del laboratorio 2": lab2,
    "nota del laboratorio 3": lab3,
    "promedio de notas":round (promedio, 1)
}
print(notas)