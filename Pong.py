import turtle
import random
import time

s = turtle.Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong by Otto")
s.tracer(0)
global st
st = 0
def start_game(x, y):
    global st
    if x > -166 and x < 166 and y > -20 and y < 85:
        st = 1
        print(st)
if st == 0:
    #start game text
    start = turtle.Turtle()
    start.penup()
    start.hideturtle()
    start.color("white")
    start.setposition(0, -50)
    start.write("START", False, align= "center", font=('impact', 100, "normal"))
    turtle.onscreenclick(start_game, 1)
print(st)
while st == 0:
    s.update()
    time.sleep(0.5)


if st == 1:
    start.undo()
    # Var
    numx = 3

    # Turtle
    timer_text = turtle.Turtle()
    timer_text.hideturtle()
    timer_text.color("white")

    #Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.color("white")
    paddle_a.shape("square")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.setposition(-350, 0)

    #Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.color("white")
    paddle_b.shape("square")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.setposition(350, 0)



    #lines
    topline = turtle.Turtle()
    topline.color("white")
    topline.shape("square")
    topline.penup()
    topline.shapesize(stretch_wid= .5, stretch_len= 40)
    topline.setposition(0, 300)

    bottomline = turtle.Turtle()
    bottomline.color("white")
    bottomline.shape("square")
    bottomline.penup()
    bottomline.shapesize(stretch_wid= .5, stretch_len= 40)
    bottomline.setposition(0, -300)

    Sideline = turtle.Turtle()
    Sideline.color("white")
    Sideline.shape("square")
    Sideline.penup()
    Sideline.shapesize(stretch_wid= 30.5, stretch_len= .5)
    Sideline.setposition(400, 0)

    Sideline2 = turtle.Turtle()
    Sideline2.color("white")
    Sideline2.shape("square")
    Sideline2.penup()
    Sideline2.shapesize(stretch_wid= 30.5, stretch_len= .5)
    Sideline2.goto(-400, 0)

    #Text
    texta = turtle.Turtle()
    texta.penup()
    texta.hideturtle()
    texta.color("white")
    texta.setposition(-120, 310)
    texta.write("00", False, align= "left", font=('impact', 50, "normal"))

    textb = turtle.Turtle()
    textb.penup()
    textb.hideturtle()
    textb.color("white")
    textb.setposition(70, 310)
    textb.write("00", False, align= "left", font=('impact', 50, "normal"))
    s.update()
    #timer Countdown
    while numx > 0:
        timer_text.clear()
        timer_text.setposition(-15, 0)
        timer_text.write(numx, font=("impact", 50, "normal"))
        numx = numx - 1
        time.sleep(1)

    timer_text.clear()
    # Line down middle
    centerline = turtle.Turtle()
    centerline.color("white")
    centerline.penup()
    centerline.hideturtle()

    for i in range(60):
        centerline.setposition(0, 300 - i * 10)
        centerline.dot(4)

    # Ball
    ball = turtle.Turtle()
    ball.color("white")
    ball.shape("square")
    ball.penup()
    ball.speed(0)
    ball.goto(0, 0)
    f = random.randint(0, 1)
    if f == 0:
        f = -1
    ball.dx = .6 * f
    ball.dy = .6
    #Points
    player_a_score = 0
    player_b_score = 0

    #Function
    global paddle_a_move
    global paddle_b_move
    global hit_count

    paddle_a_move = 0
    paddle_b_move = 0

    hit_count = 0

    #Paddle hit logic
    def paddle_hit(paddle, bx, by, bdx):
        ret = False
        # cpy = abs(paddle.ycor())
        # cpx = abs(paddle.xcor())
        py = paddle.ycor()
        px = paddle.xcor()

        if bdx < 0:
            if by - 10 < py+50 and by+10 > py - 50 and bx-10 < px+10 and bx-10 > px-10:
                ret = True
        else:
            if by - 10 < py+50 and by+10 > py -50 and bx+10 > px-10 and bx+10 < px+10:
                ret = True
        return ret

    def paddle_move(paddle, move):
        y = paddle.ycor()
        y += move * 5
        if y > 255 or y < -250:
            y -= move * 5
        paddle.sety(y)

    def changePadA(a):
        global paddle_a_move
        paddle_a_move += a
        # return a

    def changePadB(a):
        global paddle_b_move
        paddle_b_move += a

    def ball_move():
        global player_a_score
        global player_b_score
        global hit_count

        if ball.xcor() <= -330 or ball.xcor() >= 330:
            # cbx = abs(ball.xcor())
            # cby = abs(ball.ycor())
            #
            #Incramental speed increase
            if paddle_hit(paddle_a if ball.xcor() <= -330 else paddle_b , ball.xcor(), ball.ycor(), ball.dx):
                ball.dx *= -1
                ball.dx *= 1.12
                ball.dy *= 1.12
                hit_count += 1

        newx = ball.xcor() + ball.dx
        newy = ball.ycor() + ball.dy
    #player score
        if newy >= 290 or newy <= -290:
            ball.dy *= -1
        if newx > 370 or newx < -370:
            if newx > 370:
                player_a_score += 1
                ball.dx = .6
                texta.undo()
                texta.setposition(-120, 310)
                texta.write(f"{str(player_a_score).zfill(2)}", False, align="left", font=('impact', 50, "normal"))
            else:
                player_b_score += 1
                ball.dx = -.6
                textb.undo()
                textb.setposition(70, 310)
                textb.write(f"{str(player_b_score).zfill(2)}", False, align="left", font=('impact', 50, "normal"))
           #when player reaches 10
            print(f"Score PlayerA {player_a_score}  PlayerB {player_b_score}")
            if player_a_score >= 1 or player_b_score >= 1:
                ball.dx = ball.dy = 0
                #Restart Game
                def restart_game(x, y):
                    global st
                    if x > -114 and x < 126 and y > -390 and y < -330:
                        print(1)
                        st = 0
                restart = turtle.Turtle()
                restart.hideturtle()
                restart.penup()
                restart.color("white")
                restart.setposition(5, -400)
                restart.write("RESTART", align="center", font=("impact", 50, "normal"))
                turtle.onscreenclick(restart_game, 1)

            else:
                k = random.randint(0, 1)
                if k == 0:
                    k = -1
                ball.dy = .6 * k
                ball.goto(0, 0)
            newx = 0
            newy = 0
            hit_count = 0
        ball.sety(newy)
        ball.setx(newx)

    #Keybind

    # s.onkey(paddle_a_up, "w")
    # s.onkey(paddle_a_down, "s")
    # s.onkey(paddle_b_up, "Up")
    # s.onkey(paddle_b_down, "Down")
    padAOne = lambda: changePadA(1)
    padAMinus = lambda: changePadA(-1)
    s.onkeypress(padAOne, "w")
    s.onkeyrelease(padAMinus, "w")
    s.onkeypress(padAMinus, "s")
    s.onkeyrelease(padAOne, "s")

    padBOne = lambda: changePadB(1)
    padBMinus = lambda: changePadB(-1)
    s.onkeypress(padBOne, "i")
    s.onkeyrelease(padBMinus, "i")
    s.onkeypress(padBMinus, "k")
    s.onkeyrelease(padBOne, "k")

    s.listen()
    #Main game  Loop
    while True:
        s.update()
        ball_move()
        if paddle_a_move != 0:
            paddle_move(paddle_a, paddle_a_move)
        if paddle_b_move != 0:
            paddle_move(paddle_b, paddle_b_move)
# while True:
#     s.update()

