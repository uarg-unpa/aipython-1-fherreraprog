#lista vacia
numeros=[]
print(type(numeros))
#lista con datos iniciales
numeros=[10,23,-89,39]
print(numeros)
#vamos a acceder a un elmento
primer_elemento=numeros[0]
print(f"Primer elemento: {primer_elemento}")
print(len(numeros))
#recorrer la lista
for elem in numeros:
  print(elem, end=", ")
print()
#agregar un elemento al final de la lista 
numeros[len(numeros)-1]=100
print(numeros)
numeros[-1]=110
print(numeros)
#no estamos sobreescribiendo el ultimo que no existe 
#numeros[4]=120
#print(numeros)
numeros.append(4)
print(numeros)
lista_regalos=["medias","vino", "perfume"]
print(lista_regalos)
lista_regalos.append(["remera","galletas", "carbon"])
print(lista_regalos)
#insert 
numeros.insert(1,-23)
print(numeros)
#index
indice=numeros.index(110)
print(f"indice {indice}")
