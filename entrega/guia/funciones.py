def mensaje():
  print("Hola - AIPython")
mensaje()

def presentacion(nombre, apellido,domicilio):
  print(f"su nombre es : {nombre}, y su apellido es : {apellido}")
  print(f"Su domicilio, es: {domicilio}")

def suma(num1=0, num2=0):
  return num1+num2

#presentacion("Franco", "Herrera", "casa")
#presentacion(domicilio="casa",apellido="Herrera",nombre="Franco")
print(suma(6))


