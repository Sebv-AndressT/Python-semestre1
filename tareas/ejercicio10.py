nombre = input("¿cual es tu nombre? ")
direccion = input("¿cual es tu direccion? ")
ciudad = input("¿cual es tu ciudad? ")
numero = input("ingresa tu numero telefonico ")

agenda = {
    "nombre":nombre,
    "direccion":direccion,
    "ciudad":ciudad,
    "numero":numero,
}
print(agenda)

agenda["redes sociales"] = input("ingrese su usuario de Facebook, Twitter e Instagram")
print("el usuario de Facebook es:",agenda["redes sociales"][0])

print("la agenda actualizada",agenda)