import time
import os

hora = 0
minutos = 0
segundos = 0

for hora in range(24):
    for minutos in range(60):
        for segundos in range(60):
            print(f"reloj: {hora}:{minutos}:{segundos}")
            time.sleep(1)
            os.system("cls")
            segundos = segundos + 1
        else:
            minutos = minutos + 1
    else:
        hora = hora + 1
        minutos = 0