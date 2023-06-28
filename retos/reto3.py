ciudades = ["santiago", "temuco", "osorno", "punta arenas"]
indice_calidad = [134,99,245,50]

for n, e in zip(ciudades, indice_calidad):
    print(n, e)

print("la ciudad con menos ICA es",ciudades[3],"con un indice total de",indice_calidad[3])
print("la ciudad con mas ICA es",ciudades[2],"con un indice total de",indice_calidad[2])

print("la ciudad de",ciudades[0],"tiene un ICA de",indice_calidad[0],"y esta en la categoria dañina para la salud en grupos sensibles")
print("la ciudad de",ciudades[1],"con un ICA de",indice_calidad[1],"y esta en la categoria moderada para la salud")
print("la ciudad de",ciudades[2],"con un indice de",indice_calidad[2],"esta en la categoria muy dañina para la salud")
print("la ciudad de",ciudades[3],"tiene un indice de",indice_calidad[3],"y esta dentro de la categoria de buena para la salud")



