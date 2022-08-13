from turtle import Turtle

starting_positions = [(0,0),(-20,0),(-40,0)]
move_distance = 20
Up = 90
Down = 270
Left = 180
Right = 0
class Snake():

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    
    def create_snake(self):
        for position in starting_positions:
            self.add_turtle(position)
    
    def add_turtle(self,position):
            timmy = Turtle(shape="square")
            timmy.color('white')
            timmy.penup()  
            timmy.goto(position)
            self.turtles.append(timmy)

    def extend(self):
        self.add_turtle(self.turtles[-1].positiong())

    def move(self):
        for turtle_num in range(len(self.turtles)-1,0,-1):
            new_x = self.turtles[turtle_num-1].xcor()
            new_y = self.turtles[turtle_num-1].ycor()
            self.turtles[turtle_num].goto(new_x,new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != Down: 
            self.head.setheading(Up)


    def down(self):
        if self.head.heading() != Up: 
            self.head.setheading(Down)
        

    def left(self):
        if self.head.heading() != Right: 
            self.head.setheading(Left)
        

    def right(self):
        if self.head.heading() != Left: 
            self.head.setheading(Right)
    
    
        