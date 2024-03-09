numeros=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(numeros)):
  for j in range(len(numeros)):
    print(numeros[i][j])
  
for fila in numeros:
  for elemento in fila:
    print(elemento, end=",")
  print()