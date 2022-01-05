#ramo : [aprovado,[requisito1, requisito2]]
ramos = {
    'base':[True],
    'mate1':[False,['base']],
    'mate2':[False,['mate1']],
    'inferencia': [False,['mate2']],
    'econo':[False,['inferencia','mate2']],
}

while True:
    x=input('ingresa ramos aprovados(x para salir)..\n')
    if x not in ramos: # vemos si esta en la malla, sirve pa salir del ciclo de preguntas poniendo x o cualquier wea
        print('no esta ese ramo \n')
        break
    else:
        if ramos[x][0] == False:# vemos si esta aprovado el ramo

            for requisito in ramos[x][1]:#recoremos los requisitos

                if ramos[requisito][0]==False:# si el requisito es falso decimos que no se puede tomar el ramos y salimos del forloop
                    ramos[x][0] = False
                    print('no puedes tomar este ramo\n')
                    break
                else: # si es requisito es True ponemos el ramo como aprovado
                    ramos[x][0]=True
                    print('registrado exitosamente \n')

        else: # este es por si ingresa el mismo ramo 2 veces y verifica si ya lo aprovaste
            print('ya aprovaste este ramo\n')
            break





print('tus ramos disponibles son')
for i in ramos: #recoremos los elem del dicc
    if ramos[i][0]==False: # si es falso recorremos los requisitos de este
        for req in ramos[i][1]:
            if ramos[req][0]==True: # si los requisitos estan aprovados devuelve el ramo, si no ,ternima el ciclo
                print(i)
            else:
                break





