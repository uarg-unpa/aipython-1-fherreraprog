#creacion
#llamando a la funcion list
nombres=list()
#usando los corchetes
frutas=[]
#darle valores iniciales
nombres=list(['Python','AIPYTHON', 'Ambiciosa'])
frutas=["manzana",'banana','tomate','frutilla']
#intersion, este metodo toma el valor y lo coloca al final de la lista, la longuitud de la lista aumenta en uno
nombres.append('franco')
#insert, nos permite agregar un elemento en cualquier posicion
nombres.insert(0,'Miguel')
#mostrar la lista
print(nombres)
#mastrar un elemento de una determina posicion
print(nombres[0])
#saber la longuitud
print(len(frutas))
#eliminacion
del(frutas[3])
print(frutas)
#recorridos
numeros=[3,-1,3,4,5,68,8]
suma=0
for i in range (len(numeros)):
    suma=suma+numeros[i]
print (suma)
#veamos otra variante
for i in numeros:
    suma=suma+i
print(suma)
#rebanas
sub_numeros=numeros[:3]




