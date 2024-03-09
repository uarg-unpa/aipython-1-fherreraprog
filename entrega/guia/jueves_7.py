# #inmutables
# cadena="AIPYTHON"
# print(cadena[5])
# cadena[5]='h'

# Desarrollar un programa que solicite al usuario una frase y un caracter, luego:
# 1. Comprobar si el caracter se encuentra en la frase.
# 2. Si el caracter se encuentra:
#     1. Indicar la posición en la que aparece por primera vez.
#     2. Obtener una subcadena a partir de la posición del caracter.
# 3. Si el caracter no se encuentra:
#     1. Informar al usuario.
#str.find(<caracter>) indice desde donde comienza, -1

frase=input("Ingrese una frase")
caracter=input("Ingrese caracter") 
#buscar la primera aparicion del caracter
posicion=frase.find(caracter)

if posicion != -1 :
  print(f"El caracter{caracter} se encuentra en la posicion {posicion+1}")
  subcadena=frase[posicion:]
  print(f"Subcadena a partir de la posicion {posicion+1}: {subcadena}")
else:
  print(f"El caracter {caracter} no se encuentra en la frase")

