from turtle import *
import time #pa retrasar un poco la animacion
import random

pospone = 0.1 #posoner milesima de seg

score=0
highest=0

wb = Screen()
wb.title("wea")#titulo de la ventana
wb.bgcolor("black")#color de fondo
wb.setup(width=600, height=600)#tamaño de la ventana
wb.tracer(0)#supestamente hace las animaciones mas placentera

#cabeza de la shit

cabeza = Turtle()
cabeza.speed(0)
cabeza.shape("square")#forma de la wea
cabeza.color("white")
cabeza.penup()#pa quitar el rastro
cabeza.goto(0,0)#donde inicia
cabeza.direction="stop" #pa que no se mueva de una la wea

#comida
comida = Turtle()
comida.speed(0)
comida.shape("square")#forma de la wea
comida.color("red")
comida.penup()#pa quitar el rastro
comida.goto(0,100)

#lista de seg
seg=[]

#tecto
texto= Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("score:0      highest:0  ",align="center", font=("Courier", 24, "normal"))
# funciones pa mover la shit
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor() #modificamos el eje y / cabeza.ycor() esta wea es pa obt la coordenada
        cabeza.sety(y+20) # cuanto queremos que se modifique y
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+20)

#fun de cada mov
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izq():
    cabeza.direction = "left"

#conectandolo con el teclado
wb.listen() # pa que este atento al teclado
wb.onkeypress(arriba, "Up")#onkeypress =  cuando presione una tecla  y le paso parametros fun, tecla
wb.onkeypress(abajo, "Down")
wb.onkeypress(derecha, "Right")
wb.onkeypress(izq, "Left")


while True:
    wb.update()

    #coliciones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() < -280 or cabeza.ycor() > 280:
        time.sleep(1) #pausa el juego
        cabeza.goto(0,0) #reinicia la serp
        cabeza.direction = "stop"
        #esconder seg
        for segmento in seg:
            segmento.goto(2000,2000)
        #limpiar lista
        seg.clear()
        score=0
        texto.clear()
        texto.write(f"score:{score}     highest:{highest}  ", align="center", font=("Courier", 24, "normal"))

    #cuando come la wea
    if cabeza.distance(comida) < 20: #si la distancia de el objeto con la wea de dentro
        x = random.randint(-280,280) # va a una posicion random/ dejamos un margen pa que la wea no desaparezca
        y = random.randint(-280, 280)
        comida.goto(x,y)

        nuevo_seg = Turtle()
        nuevo_seg.speed(0)
        nuevo_seg.shape("square")  # forma de la wea
        nuevo_seg.color("grey")
        nuevo_seg.penup()  # pa quitar el rastro
        seg.append(nuevo_seg)

        #aumentar marcador
        score+=10

        if score > highest:
            highest = score
        texto.clear()
        texto.write(f"score:{score}     highest:{highest}  ", align="center", font=("Courier", 24, "normal"))

    #agregar el seg a la serp
    totalseg= len(seg)
    for i in range(totalseg-1,0,-1):
        x=seg[i-1].xcor() #coordenadas del seg anterior
        y = seg[i-1].ycor()
        seg[i].goto(x,y)

    if totalseg > 0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        seg[0].goto(x,y)

    mov() # llamamos la func

    #colision cuerpo
    for segmento in seg:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

        # esconder las weas
            for segmento in seg:
                segmento.goto(2000,2000)
            seg.clear()

            score=0

            texto.clear()
            texto.write(f"score:{score}     highest:{highest}  ", align="center", font=("Courier", 24, "normal"))



    time.sleep(pospone)#con esta shit posponemos la shit