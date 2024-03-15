#Alcances y mas
#una variable vive fuera de la funcion y se puede usar en el cuerpo de la misma

num=2
def multiplicacion(x):
  return num*x
print(multiplicacion(7))

#
def multi(x):
  num=3
  return num*x
print(multiplicacion(7))

#una variable solo vive en la funcion y ese es su alcance
#poner en otro archivo
def suma(x):
  num=5
  return x+num
print(suma(3))
print(num)

#preguntas para los alumnos
def mensaje():
  alt=1
  print("Hola estudiantes de AIPython")
print(alt) #error

a=1
def fun():
  a=3
  print(a)

fun()
print(a)
#3
#1

