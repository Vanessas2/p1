import turtle

pegasus = turtle.Turtle()
#cria pegasus
pegasus.getscreen().bgcolor("black")
#muda o fundo da tela para cor que eu escolher

pegasus.penup()
pegasus.goto((-200,100))
pegasus.pendown()
#utilizado pra iniciar pegasus no ponto que eu quero


def star (turtle, size):
    turtle.color("yellow")
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        #liga uma forma a outra, imediatamente antes de desenhar a proxima
        for i in range (5):
            turtle.forward(size)
            #move para frente
            star(turtle, size/3)
            turtle.left(216)
            #gira a tartaruga pro angulo que eu informo

 
star(pegasus,360)
#chama a função pegasus





turtle.done()
