dia = input("Introduce el día de la semana: ")
dia=dia.title()
match dia:
    case "Lunes":
        print("Hoy es lunes, ¡a trabajar!")
    case "Martes":
        print("Hoy es martes, ¡que tengas un buen día!")
    case "Miércoles":
        print("Hoy es miércoles, ¡ya casi es fin de semana!")
    case "Jueves":
        print("Hoy es jueves, ¡un poco más para el viernes!")
    case "Viernes":
        print("¡Hoy es viernes, fin de semana!")
    case _:
        print("Día no válido.")