def mostrarCarac(palabra):
  for i in range(len(palabra)):
    print(palabra[i])
    
def contarVocales(palabra):
  cant=0
  for i in range(len(palabra)):
    if palabra[i]=='a' or palabra[i]=='e' or palabra[i]=='i' or palabra[i]=='o' or palabra[i]=='u':
      cant=cant+1
  return cant

def contarCons(palabra):
  cant=0
  for letra in palabra:
    if letra != 'a' and letra!='e' and letra!='i' and letra !='o' and letra !='u':
      cant+=1
  return cant

def buscarSimbolo(simbolo, palabra):
  for letra in palabra:
    if letra==simbolo:
      return True
  return False

def invertirPalabra(palabra):
  return palabra[::-1]
  


def main():
  while True:
    palabra=input("Ingrese una palabra: ")
    print("1: Mostrar Caracteres ")
    print("2: Cantidad de Vocales ")
    print("3: Cantidad de Consonantes ")
    print("4: Buscar un simbolo en la palabra")
    print("5: Invertir Palabra")
    op=int(input("Ingrese su opcion: "))
    if op == 1:
      mostrarCarac(palabra)
    elif op == 2:
      print(f"La cantidad de vocales en {palabra} es {contarVocales(palabra)}")
    elif op == 3:
      print(f"La cantidad de consonantes en {palabra} es {contarCons(palabra)}")
    elif op == 4:
      simbolo=input("Ingrese para buscar: ")
      if buscarSimbolo(simbolo, palabra):
        print(f"el {simbolo} se encuentra en {palabra}")
      else:
        print("Esta vez no lo encontramos")
    elif op == 5:
      invertida=invertirPalabra(palabra)
      print(invertida)
    else:
      print("Parece no haber ingresado una opcion disponible ")
    cont=input("Desea Continuar? s|n")
    if cont=='s' or cont=='S':
      continue
    else:
      break
  print("Finalizado")
  
main()
      

