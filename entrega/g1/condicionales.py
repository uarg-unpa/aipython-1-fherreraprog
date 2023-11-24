numero1= int(input("Ingrese un numero: "))
numero2=input("Ingrese otro numero: ")#string
numero2=int(numero2)#casting a int
if numero1>numero2:
  mayor=numero1
else:
  mayor=numero2
print(f"el mayor es {mayor}")

positivos=0
negativos=0
num=int(input("Ingrse numero: "))
while num != 0:
  if num > 0 :
    positivos=positivos+1
  else:
    negativos=negativos+1
  num=int(input("Ingrese numero: "))
print(f"Numeros positivos {positivos}")
print(F"Numeros negativos {negativos}")
palabra= "AIPython P1"

print("Vamos a simular los errores de internet")
error=403
match error:
  case 400:
   print ("Bad request")
  case 404:
    print ("Not found")
  case 418:
    print ("I'm a teapot")
  case 401 | 403 | 404:
   print ("Not allowed")
  case _:
    print ("Something's wrong with the internet")