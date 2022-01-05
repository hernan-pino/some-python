ramos={'eco':[6, {"lunes":0,"miercoles":2}], 'intro':[4, '1b'], 'fisica':[7, '2b']} 
horario = {"lunes":["","","","",""],"martes":["","","","",""],"miercoles":["","","","",""],"jueves":["","","","",""],"viernes":["","","","",""]}
creditos=12

print('los ramos diponibles son:')
for i in ramos:
    print(i)
while True:
    ramo = input('ingrese el ramo que quiere tomar: ')
    bloques_del_ramo = ramos[ramo][1]
    for bloque in bloques_del_ramo:
        if horario[bloque][bloques_del_ramo[bloque]]!= "":
              print("Error el boque esta ocupado")
        else: 
            horario[bloque] = ramo
            creditos-=ramos[ramo][0]

            print(f'te quedan {creditos} disponibles')



