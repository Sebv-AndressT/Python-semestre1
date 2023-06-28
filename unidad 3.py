num = 0 
"""while num <= 100:
    print(num)
    num += 2 """ #igual puede se num = num+2

#while infinito

#while true:
#print(num)
#num +=2
#while (else/if)

while num <= 100:
    print(num)
    num += 2
else:
    print("mi condicion es igualo mayor a 100")

#uso del break
while True:
    parametro = input("<")
    if parametro == "exit":
        break
    print(parametro) 
    

#24-05
num = 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)

#for
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

