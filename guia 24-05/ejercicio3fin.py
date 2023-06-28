#Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada uno). 
#Se busca calcular el pago diario y el total semanal de 
#cada empleado de acuerdo con los siguientes puntos:

print()
print("Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada uno. Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo con los siguientes puntos:")                     
print()
print("La tarifa de las horas diurnas es de 12000 CLP.")
print("La tarifa de las horas nocturnas es de 16000 CLP.")
print("Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el turno nocturno.")

#a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves y Viernes en turnos diurnos.
#b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tambien el dıa domingo en turno diurno.
#c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, Sabado y Domingo en turnos nocturnos.
print()
#pago por hora
td=12000*10
tn=16000*10
domtd=12000*10+2000*10
domtn=16000*10+3000*10



#diccionario empleados
empleado1={
"pago dia lunes":tn, #160000
"pago dia martes":tn, #160000
"pago dia miercoles":tn, #160000
"pago dia jueves":td, #12000
"pago dia viernes":td, #120000
"pago semanal total": tn*3+td*2
}
empleado2={
"pago dia martes":tn, #160000
"pago dia miercoles":tn, #160000
"pago dia jueves":tn, #160000
"pago dia domingo":domtd, #140000
"pago semanal total":tn*3+domtd
}
empleado3={
"pago dia miercoles":td, #120000
"pago dia jueves":td, #120000
"pago dia viernes":td, #120000
"pago dia sabado":tn, #160000
"pago dia domingo":domtn, #190000
"pago semanal":td*3+tn+domtn
}


print("datos empleado1:",empleado1)
print(2)
print("datos empleado2:",empleado2)
print()
print("datos empleado3:",empleado3)
print()

