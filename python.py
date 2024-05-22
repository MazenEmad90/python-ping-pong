#mazen emad 
#import turtle
import turtle

wind= turtle.Screen()
wind.title("ping pong By mazen")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)
#madreb1
madreb1 = turtle.Turtle()
madreb1.speed(0)
madreb1.shape("square")
madreb1.color("blue")
madreb1.shapesize(stretch_wid=6, stretch_len=1)
madreb1.penup()
madreb1.goto(-350, 0)
#madreb2
madreb2 = turtle.Turtle()
madreb2.speed(0)
madreb2.shape("square")
madreb2.color("red")
madreb2.shapesize(stretch_wid=6, stretch_len=1)
madreb2.penup()
madreb2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3
#to work madrab1
def madrab1_up():
    y = madreb1.ycor()
    y += 20 
    madreb1.sety(y)

def madrab1_down():
    y = madreb1.ycor()
    y -= 20 
    madreb1.sety(y)
#to work madrab2
def madrab2_up():
    y = madreb2.ycor()
    y += 20 
    madreb2.sety(y)

def madrab2_down():
    y = madreb2.ycor()
    y -= 20 
    madreb2.sety(y)

#madrab1
wind.listen()
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
#madrab2
wind.listen()
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")
#

#
while True:  
    wind.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx*=-1
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx*=-1
    #
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()<madreb2.ycor() + 40 and ball.ycor() > madreb2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
        
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()<madreb1.ycor() + 40 and ball.ycor() > madreb1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        #mazen emad
        