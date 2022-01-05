# ramo: [credito, [blocke,blocke]]
ramos={'eco':[6, ['1a','3b']], 'intro':[4, ['1a','4b']], 'fisica':[7, ['2b','3a']]}

bolck={"1a":'','1b':'','2a':'','2b':'','3a':'','3b':'','4a':'','4b':''}
creditos=20

def semana():
    print(" ", "  lun ", "  martes ", "  mier ", "  juev ")
    print('--------------------------------------')
    print('a', '  ',bolck['1a'],'  ',bolck['2a'],'  ',bolck['3a'],'  ',bolck['4a'])
    print('--------------------------------------')
    print('b','  ', bolck['1b'],'  ', bolck['2b'],'  ', bolck['3b'],'  ', bolck['4b'])

# mostramos los nombres de los ramos disponibles
print('los ramos diponibles son:')
for i in ramos:
    print(i)
print('\n')

# mientras tengas creditos disponibles
while creditos > 0:

    x=input('ingrese ek ramo que quiere tomar:  ')
    print('')
    if x in ramos:# si el ramo esta en la lista de ramos

        for i in range(len(ramos[x][1])):# ve todos lo bloques que tiene este ramo

            y=ramos[x][1][i]# y es el bloque

            if bolck[y]!='':# ve si el blocke esta ocupado
                print('ta usa la wea')
                print('')
                creditos+=ramos[x][0]#resetea los creditos
                break

            else: # si esta disponible agrea el ramo al blocke
                bolck[y] = x

        creditos -= ramos[x][0] # resta los creditos del ramo del contador

        semana()# mostramos el horario


        print(f'te quedan {creditos} disponibles \n')