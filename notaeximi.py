# peso de cada wea
peso_nota=.3
peso_solemne=.3
peso_examen=.4
lista_nota=[]
solemne=1


def menu():

    print("MENU\n")
    print("1. ingresar notas\n")
    print("2. ingresar solemnes\n")



while True:
    menu()
    opcion = int(input("elige una opcion "))
    while opcion==1:
       print("  ")
       nota=int(input("ingrese nota.. "))
       lista_nota.append(nota)
       promedio_nota = sum(lista_nota) / len(lista_nota)

       otraopcion=int(input("1. mas notas    2. salir  "))

       if otraopcion==2:
           break

    else:
        if opcion==2:
         solemne=int(input("dime tu nota solemne"))
        break




ponderacion_nota = promedio_nota * peso_nota
ponderacion_solemne = solemne * peso_solemne
necesito = ((ponderacion_nota + ponderacion_solemne - 40) / peso_examen)*-1
print("")
print("tus notas son", lista_nota)
print("necesitas", necesito, "para pasar")

