import random
#var
jugando=True
jugador="X"
ganador=None


# el tablero
theboard = {"1": 1, "2": 2, "3": 3,
            "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9}

#  imprime el tablero
def iboard():
    print("         ")
    print(theboard["1"], "|", theboard["2"], "|", theboard["3"])
    print("---------")
    print(theboard["4"], "|", theboard["5"], "|", theboard["6"])
    print("---------")
    print(theboard["7"], "|", theboard["8"], "|", theboard["9"])

# imprime le menu de incicio
def dmenu():
    print("***************")
    print("WELCOME TO GATO\n")
    print("1. player v/s player")
    print("2 player v/s BOT")
    print("3. salir\n")

# dinamica de turno
def turno():
    posicion=input("elige una posicion.. ")
    theboard[posicion]="X"


iboard()
while True:
    turno()
    iboard()