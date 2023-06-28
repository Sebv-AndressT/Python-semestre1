hora = 0
minutos = 0
segundos = 0

while hora <= 0:
    hora += 0
    if hora == 0:
        print(f"hora:{hora}")
        while minutos <= 59:
             minutos += 1
             if minutos == 59:
                 print(f"minutos:{minutos}")
                 while segundos <= 59:
                     segundos += 1
                     if segundos == 59:
                          print(f"segundos:{segundos} ")

print(f"hora:{hora}:{minutos}:{segundos}")

