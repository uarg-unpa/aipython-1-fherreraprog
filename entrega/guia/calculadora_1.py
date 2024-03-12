#Calculadora AIPython, solo trabaja con dos numeros enteros
#vamos a permitir que pueda repetir mas de una operacion
print("Bienvenidos a la calculadora AIPython P1")
op=0
while True :
  print(f"1: Para sumar  ")
  print(f"2: Para restar  ")
  print(f"3: Para multiplicar  ")
  print(f"4: Para dividir  ")
  print(f"5: Para calcular la potencia ")
  print(f"6: Para obtener la division entera entre  ")
  print(f"7: Para Finalizar ")
  op=int(input("Ingrese la opcion para operar con los numeros: "))
  if op >= 1 and op <=6 : 
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
  if op == 1:
    suma=num1+num2
    print(f"La suma es {suma}")
  elif op == 2:
    resta=num1-num2
    print(f"La resta es {resta}")
  elif op == 3:
    producto=num1*num2
    print(f"El producto es {producto}")
  elif op == 4:
    division=num1/num2
    print(f"La division es  {division}")
  elif op == 5 :
    potencia= num1**num2
    print(f"La potencia es {potencia}")
  elif op == 6 :
    division_entera= num1//num2
    print(f"La division entera es {division_entera}")
  elif op == 7 :
    print("Adios vuelva pronto!!")
    break 
  elif op!= 7:
    print(f"Parece que {op} aun no esta definida entre las opciones \nprobemos de nuevo !!")
    continue

 