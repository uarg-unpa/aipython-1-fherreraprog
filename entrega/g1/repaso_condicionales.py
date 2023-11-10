
while condicion :
  sentencia1

#Condicion es verdadera ->  infinitas veces
#condicion es falsa -> nunca 

cont=6 #cont=0
while cont!=5 : 
  cont=cont+1 #cont=cont-1
  
cont=1
while cont<5 :
  cont=cont-1 #cont=cont+1

#cual es el problema
cont=1
suma=0
while cont <=10 :
  suma=suma+cont
  cont=cont+1

num=int(input())
suma=0
while(num!=0):
  print(num)
  suma=suma+num
  num=int(input())
  
enunciado1
while condicion1:
	enunciado2
enunciado3
enunciado4

num=int(input())
while(num<10):
	print(f'el numero es, {num}')
	num=num+1  
 #num=1. #9
 #num=10. #

 
cont=1
while(      cont<6              ): # cont <=5
	num=int(input())
	print(f"El num ingresado es {num}")
	cont=cont+1
 
opcion=input('ingrese opcion')
while(    opcion!= 'A'     ):
	print(opcion)
	opcion=input()
 
cont=0
sumatoria=0
while(cont<=10):
	num=int(input())
  sumatoria=sumatoria+num
	cont=cont+1
 
contpar=0
contimpar=0
for _ in range(20):
	num=int(input("ingrese num"))
	if num%2==0:
		contpar=contpar+1
	else:
    contimpar=contimpar+1
print(cantpar)
print(cantimpar)

#Leer tres numero enteros, num1, num2, num3, calcular e imprimir el producto y la suma entre ellos.
num1=int(input("Ingrese num1"))
num2=int(input("Ingrese num2"))
num3=int(input("Ingrese num3"))
suma=num1+num2+num3
producto=num1*num2*num3
print(F"La suma es {suma} y el producto es {producto}")

#Repetir lo anterior pero esta vez, para los tres números utilizar solo variable num
num=int(input("Ingrese un numero: "))
cont=1
suma=0
producto=1
while cont <= 3:
  suma=suma+num
  producto=producto*num
  num=int(input("Ingrese otro numero: "))
  cont=cont+1
print(f"La suma es {suma}")
print(f"El producto es {producto}")

####
suma=0
producto=1
for _ in range(3):
  num=int(input("Ingrese un numero: "))
  suma=suma+num
  producto=producto*num
print(f"La suma es {suma} y el producto es {producto}")

#Realizar un bucle que lea cinco números y escribir el menor de todos 

menor=int(input("Ingrese numero"))
for _ in range(4):
  num=int(input("Ingrese numero: "))
  if num < menor:
    menor=num
print(f"El menor de cinco numeros es {menor}")

cont=0
while cont < 5:
  print (cont)
  cont=cont+1
  if cont == 3:
    break

cont=0
while cont < 5:
  if cont == 3:
    cont=cont+1
    continue
  print(cont)
  cont=cont+1
