a = [500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800]
b = [456, 454, 452, 450, 448, 446, 444, 442, 440, 438, 436, 434, 432, 430, 428, 426, 424, 422, 420, 418, 416, 414, 412, 410, 408, 406, 404, 402, 400, 398, 396]


print("comienzo")
for n, e in zip(a, b):
    print(f"{n} + {e} = {n + e}")
print("final")

resultado = a + b
print("la suma total es de:",sum(resultado))
