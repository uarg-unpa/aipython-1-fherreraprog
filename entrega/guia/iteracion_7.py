# #mostrar los numeros desde el 0 hasta el 10
# contador=0
# while contador <= 10:
#   print(contador, end='-')
#   contador=contador+1
# print()
# print("Fin de la iteracion")
# #for
# cadena="AIPYTHON"
# for letra in cadena:
#   print(letra)
# #range()
# for num in range(11):
#   print(num)
# #
# for indice in range(len(cadena)):
#   print(cadena[indice])
# # imprimir 10 veces AIPYTHON
# for _ in range(5):
#   print("AIPYTHON")

respuesta=input("como vas con las guias: ")
respuesta=respuesta.lower()
if "bien" in respuesta or "muy bien" in respuesta or 'ok' in respuesta:
  print("Me alegro, estas progresando!!")
elif "maso" in respuesta or "ahi voy" in respuesta or "nah" in respuesta:
  print("No dudes en consultar, la practica es la solucion")
else:
  print("ouch 😫")