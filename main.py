import turtle
import winsound

def paddle_a_up():
                y = paddle_a.ycor()
                y +=20
                paddle_a.sety(y)

def paddle_a_down():
                y = paddle_a.ycor()
                y -=20
                paddle_a.sety(y)

def paddle_b_up():
                y = paddle_b.ycor()
                y +=20
                paddle_b.sety(y)

def paddle_b_down():
                y = paddle_b.ycor()
                y -=20
                paddle_b.sety(y)

winsound.PlaySound('Eva pong song tema.wav', winsound.SND_ASYNC)
game = turtle.Screen()
game.title("Ping Pong")
game.bgpic("E:\Programação\Para o Git\Ping pong\Eva pong.png")
game.setup(800,800)
game.tracer(0)

point_a = 0
point_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-195, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(175, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1.2, stretch_len=1.2)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Team Blue: 0  Eva: 0", align="center", font=("Fantasy", 24, "normal"))

game.onkeypress(paddle_a_up, "Up")
game.onkeypress(paddle_a_down, "Down")
          
while True:
    game.update()
    game.listen()
              
    if point_a == 3:
        pen.clear()
        pen.write("Você ganhou",align="center", font=("Fantasy", 24, "normal"))
        winsound.PlaySound('Victory.wav', winsound.SND_ASYNC)
        game.exitonclick()

    if point_b == 3:
        pen.clear()
        pen.write("Red ganhou",align="center", font=("Fantasy", 24, "normal"))
        winsound.PlaySound('Defeat.wav', winsound.SND_ASYNC)
        game.exitonclick()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 125:
        ball.sety(125)
        ball.dy *= -1
    
    if ball.ycor() < -70:
        ball.sety(-70)
        ball.dy *= -1

    if ball.xcor() > 200:
        ball.goto(0,0)
        point_a += 1
        pen.clear()
        pen.write("Team Blue: {}  Team Red: {}".format(point_a, point_b), align="center", font=("Fantasy", 24, "normal"))
        ball.dx *= -1
    
    if ball.xcor() < -200:
        ball.goto(0,0)
        point_b +=1
        pen.clear()
        pen.write("Team Blue: {}  Team Red: {}".format(point_a, point_b), align="center", font=("Fantasy", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() < -185 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 15:
        ball.dx *= -1 
    
    elif ball.xcor() > 165 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 15:
        ball.dx *= -1

    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 38:
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 48:
        paddle_b_down()