#mostrar los numeros desde el 0 hasta el 10
contador=0
while contador <= 10:
  print(contador, end='-')
  contador=contador+1
print()
print("Fin de la iteracion")
#for
cadena="AIPYTHON"
for letra in cadena:
  print(letra)
#range()
for num in range(11):
  print(num)
#
for indice in range(len(cadena)):
  print(cadena[indice])
# imprimir 10 veces AIPYTHON
for _ in range(5):
  print("AIPYTHON")