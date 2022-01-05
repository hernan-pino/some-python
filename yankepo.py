import random

def yankenpo(jugador1,jugador2):
    gano=True
    if jugador1=="piedra":
        if jugador2=="papel":
            gano=False
        elif jugador2=="tijera":
            gano=True
    elif jugador1=="tijera":
        if jugador2=="piedra":
            gano=False
        elif jugador2=="papel":
            gano=True
    else:
        if jugador2=="tijera":
            gano=False
        elif jugador2=="piedra":
            gano=True
    return gano

win1=0
win2=0
cpu=["piedra","papel","tijera"]
juegos=100
n=20000

while juegos<=n:
    jugador1 = random.choice(cpu)
    jugador2 = cpu[random.randint(0,2)]
    #print("jugador 2:",jugador2)

    if jugador1!=jugador2:
        x=yankenpo(jugador1,jugador2)
        if x==True:
            win1+=1
            # print(f"{win1}-{win2}")
        else:
            win2+=1
            # print(f"{win1}-{win2}")
    # else:
    #     print("empate")
    #     print(f"{win1}-{win2}")
    juegos+=1

winrate1=(win1/n)*100
winrate2=(win2/n)*100
empate=n-(win1+win2)
empaterate=(empate/n)*100


print(f"j1 gana un {round(winrate1)}% "
      f"j2 gana un {round(winrate2)}% "
      f"empate {round(empaterate)}% ")