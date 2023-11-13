#definicion de funciones
def suma(num1,num2):
  return num1+num2

def saludo(nombre="AIPython P1"):
  return f"Te damos la bienvenida {nombre}"

#crear la tabla de multiplicar de un x
def tabla(num=6):
  for i in range(1,11):
    print(f"{i} x {num} = {i*num}")
  
def par_impar(num):
  if num%2==0:
    return True
  else:
    return False

def par_imparf(num):
  return num%2==0

def mayor_de_tres(num1, num2, num3):
  mayor=num1
  if num2 > mayor:
    mayor=num2
  if num3 > mayor:
    mayor=num3
  return mayor
#retornar la suma de los elementos de la lista
def suma_lista(lista):
  return sum(lista)

def suma_lista2(lista):
  suma=0
  for elemento in lista:
    suma=suma+elemento
  return suma

def suma_lista3(lista):
  suma=0
  for i in range(len(lista)):
    suma=suma+lista[i]
  return suma
#invocaciones
def main():
  resultado=suma(5,6)
  print(resultado)
  print(saludo("Fernanda"))
  print(saludo())
  suma_lista([3,4,5])
  tabla(8)

main()