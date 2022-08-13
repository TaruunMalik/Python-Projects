from turtle import Turtle,Screen
import random

is_racing = False
screen = Screen()
screen.setup(width=1000,height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: ")
print(user_input)

colors = ['purple','green','yellow','blue','violet','red']
y_position = [-70,-40,-10,20,50,80]
all_turtles = []

for turtles in range(0,6):
    timmy = Turtle(shape='turtle')
    timmy.penup()
    timmy.goto(x=-480,y=y_position[turtles])
    timmy.color(colors[turtles])
    all_turtles.append(timmy)
if user_input:
    is_racing = True

while is_racing:
    for a_turtle in all_turtles:
        if a_turtle.xcor()>480:
            is_racing = False
            winner_turtle = a_turtle.pencolor()
            if winner_turtle==user_input:
                print("YAY! You've won the bet!")
            else:
                print(f"You've lost, {winner_turtle} turtle won the race.")
        turt_distance = random.randint(0,10)
        a_turtle.forward(turt_distance)


screen.exitonclick()
