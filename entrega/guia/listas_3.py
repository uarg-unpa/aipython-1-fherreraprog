def numeros_pares(n):
  pares=[]
  for i in range(n+1):
    if i % 2 == 0 :
      pares.append(i)
  return pares
print(numeros_pares(7))
resultado=numeros_pares(7)
#resulado es una lista

