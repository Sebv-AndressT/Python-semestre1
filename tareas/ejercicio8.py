mes = input("ingrese un mes del caledario ")

estaciones = {
    "enero":"verano",
    "febrero":"verano",
    "marzo":"verano",
    "abril":"otoño",
    "mayo":"otoño",
    "junio":"invierno",
    "julio":"invierno",
    "agosto":"invierno",
    "septiembre":"invierno",
    "octubre":"primavera",
    "noviembre":"primavera",
    "diciembre":"verano",
}

if mes in estaciones:
    estacion = estaciones[mes]
    print("el mes",mes,"corresponde a la estacion",estacion)
else:
    print("ingrese un mes que este en el calendario por favor")
