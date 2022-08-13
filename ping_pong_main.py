import time
from paddles import Paddle,Ball,Scoreboard
from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PING PONG!")
screen.tracer(0)


r_paddle =Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')


game_on = True
while game_on:
    
    screen.update()
    time.sleep(ball.moving_speed)
    ball.moving()

    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bouncing_y()

    if ball.distance(r_paddle)< 50 and ball.xcor() > 320:
        ball.bouncing_x()
       
    
    if ball.distance(l_paddle)< 50 and ball.xcor() < -320:
        ball.bouncing_x()
        

    if ball.xcor()> 390 :
        ball.out_of_bonds()
        score.l_scored()
        
    if ball.xcor() < -390:
        ball.out_of_bonds()
        score.r_scored()
       
screen.exitonclick()