num=int(input())
while num > 0:
    if num%2==0:
        print("Finalizando el bucle")
        break
    num=int(input())


suma=0
for i in range(1,30):
    print (i)
    if i > 10:
        continue
    suma=suma+i
print (suma)
