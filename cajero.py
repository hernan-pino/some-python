print("Hola welcome to HP bancos\n")

# definimos variables clave

clave = 1234
intentos = 3
balanse = 100000
inicio = 0

# iniciamos el loop con while

while intentos >= 0:
    pin = int(input("ingresar clave de 4 digitos\n"))
    if pin == clave:
        while inicio == 0:
            print("Elija una pcion\n")
            print("1. Realizar un giro\n")
            print("2. Realizar un deposito\n")
            print("3. Cambio de clave\n")
            print("4. salir\n")
            opcion = int(input("elija una opcion"))
            if opcion == 1:
                giro = int(input("ingrese el monto a girar $"))
                balanse = balanse - giro
                print("tu nuevo saldo es de $", balanse)
                salir1 = int(input("desea alguna otra operacion\n"
                                   "1.si 2.no"))

                while salir1 > 2:
                    salir1 = int(input("esta opcion no existe, elija nuevamente "))
                if salir1 == 2:
                    break

            elif opcion == 2:
                deposito = int(input("ingrese el monto a depositar $"))
                balanse = balanse + deposito
                print("su nuevo saldo es de $", balanse)
                salir1 = int(input("desea alguna otra operacion\n"
                                   "1.si 2.no "))

                while salir1 > 2:
                    salir1 = int(input("esta opcion no existe, elija nuevamente "))
                if salir1 == 2:
                    break

            elif opcion == 3:
                pin = int(input("ingresar clave actual\n"))
                while pin != clave:
                    pin = int(input("clave incorrecta, intenta nuevamente"))

                if pin == clave:
                    clave = int(input("ingresa tu nueva clave (4 digitos)"))
                    while len(str(clave)) != 4:
                        if len(str(clave)) > 4:
                            clave = int(input("muy larga"))
                        else:
                            clave = int(input("muy corta"))

                    else:
                        print("tu clave ha sido cambiada exitosamente")

                salir1 = int(input("desea alguna otra operacion\n"
                                   "1.si 2.no"))
                while salir1 > 2:
                    salir1 = int(input("esta opcion no existe, elija nuevamente"))
                if salir1 == 2:
                    break

            elif opcion == 4:
                print("xau gracias")
                break
            else:
                print("opcion no valida\n")
                opcion = int(input("elija una opcion"))

    elif pin != clave:
        print("te equivicaste ql")
        intentos = intentos - 1
        if intentos == 0:
            print("blokiao por wn")
            break
