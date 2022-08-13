from time import time
from turtle import Turtle,Screen, xcor, ycor
import time
from snake import Snake
from snakes import Food
from snake_scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

snake = Snake()
foods = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

   

game_live = True

while game_live:
    screen.update()
    time.sleep(0.08)
    snake.move()
    
     
    # EATING FOOD
    if snake.head.distance(foods)<18:
        foods.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detect collision with tail/body:
    for segment in snake.turtles:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_live = False
            scoreboard.game_over()



screen.exitonclick()
