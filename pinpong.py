import turtle
import os

win = turtle.Screen()
win.title('Ping Pong')
win.bgcolor('blue')
win.setup(width=800, height=600)
win.tracer(0)

# Scores
scoreA = 0
scoreB = 0


"""
paddles
"""

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


paddleB =turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('red')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)


""" Ball"""
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

""" Score board"""
board = turtle.Turtle()
board.speed(0)
board.color('white')
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write('Player A: 0    Player B: 0 ', align='center', font=('Arial', 24, 'normal'))


def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


win.listen()
win.onkeypress(paddleAUp, 'v')
win.onkeypress(paddleADown, 'b')
win.onkeypress(paddleBUp, 'Up')
win.onkeypress(paddleBDown, 'Down')



while True:
    win.update()

    """ Ball movement"""
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    """ Border check """
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('aplay bounce.wav&')

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('aplay bounce.wav&')

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        board.clear()
        board.write('Player A: {}    Player B: {} '.format(scoreA, scoreB), align='center', font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        board.clear()
        board.write('Player A: {}    Player B: {} '.format(scoreA, scoreB), align='center',
                    font=('Arial', 24, 'normal'))

    """ Ball and Paddles collision """
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system('aplay bounce.wav&')

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor()- 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system('aplay bounce.wav&')