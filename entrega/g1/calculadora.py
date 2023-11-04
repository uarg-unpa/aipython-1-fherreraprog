#Solo opera con dos numeros enteros
print("Bienvenidos a la calculadora AIPython P1")
cant_ope=0
sumas=0
restas=0
op=0
while op!= 7 :
  num1=int(input("Ingrese el primer numero: "))
  num2=int(input("Ingrese el segundo numero: "))
  print(f"1: Para sumar {num1} y {num2} ")
  print(f"2: Para restar {num1} y {num2} ")
  print(f"3: Para multiplicar {num1} y {num2} ")
  print(f"4: Para dividir {num1} y {num2} ")
  print(f"5: Para calcular la potencia {num1} y {num2} ")
  print(f"6: Para obtener la division entera entre {num1} y {num2} ")
  print(f"7: Para Finalizar ")
  op=int(input("Ingrese la opcion para operar con los numeros: "))
  if op == 1:
    suma=num1+num2
    cant_ope=cant_ope+1
    sumas=sumas+1
    print(f"La suma es {suma}")
  elif op == 2:
    resta=num1-num2
    cant_ope=cant_ope+1
    restas=restas+1
    print(f"La resta es {resta}")
  elif op == 3:
    producto=num1*num2
    cant_ope=cant_ope+1
    print(f"El producto es {producto}")
  elif op == 4:
    division=num1/num2
    cant_ope=cant_ope+1
    print(f"La division es  {division}")
  elif op == 5 :
    potencia= num1**num2
    cant_ope=cant_ope+1
    print(f"La potencia es {potencia}")
  elif op == 6 :
    division_entera= num1//num2
    cant_ope=cant_ope+1
    print(f"La division entera es {division_entera}")
  elif op!= 7:
    print(f"Parece que {op} aun no esta definida entre las opciones")
  
  if op == 7:
    op='n'
  else :
    op=input("Desea continuar s, si : ")
  if op.casefold()== 'n' or op.casefold() == 'no' :
    op=7
    print("Adios vuelva pronto!!")
print(f"La cantidad de operaciones que realizo durante el uso de la calculadora fueron {cant_ope}")
print("sumas\t restas\t")
print(f"{sumas}\t {restas}")

