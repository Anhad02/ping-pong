import turtle
import winsound
import time

wn=turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0

#Paddle 1
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle 2
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

#Function A UP
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

#Function A down
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#Function B UP
def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

#Function B down
def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

    
#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))
    

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")



#Main Game Loop
while True:
    time.sleep (1/120)
    wn.update()
    #Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Check UP
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Border Check DOWN
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Border Check RIGHT
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    #Border Check LEFT
    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
