# edad = int(input("Introduci tu edad: "))
# tiene_dinero = input("Tenes dinero? (si/no) ")
# if edad >= 18 and tiene_dinero == "si":
#     print("podes entrar al casino.")
# else:
#     print("No podes entrar al casino.")

#Rebanadas
#['A I P Y T H O N']
#  0 1 2 3 4 5 6 7
#-   7 6 5 4 3 2 1
oracion="A veces la persona que nadie imagina capaz de nada es la que hace cosas que nadie imagina"
#cadena[inicio:fin:paso]
primera_palabra=oracion[-7:]
cada_tres=oracion[2::3]
print(len(oracion))
print(f"La primera palabra es {primera_palabra}")
print(f"La primera palabra es {cada_tres}")
invertir_oracion=oracion[::-1]
print(invertir_oracion)

#operador in y not in
if "Persona" in oracion:
  print("Persona es una palabra que forma la oracion ")