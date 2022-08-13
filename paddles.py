from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        # self.speed('fastest')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor()<250 :
            new_y= self.ycor()+25
            self.goto(self.xcor(),new_y)
        

    def down(self):
        if self.ycor()>-250:
            new_y = self.ycor() - 25
            self.goto(self.xcor(),new_y)
        
    

class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1
    def moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bouncing_y(self):
        self.y_move *= -1
        
    def bouncing_x(self):
        self.x_move *= -1
        self.moving_speed *= 0.83

    def out_of_bonds(self):
        self.goto((0,0))
        self.bouncing_x()
        self.moving_speed = 0.1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('cyan')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0 
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"P2: {self.l_score}",align = 'center' ,font=('arial',30,'normal'))
        self.goto(100,250)
        self.write(f"P1: {self.r_score}",align = 'center' ,font=('arial',30,'normal'))
        


    def l_scored(self):
        
        
        self.l_score += 1
       
        self.increase_score()
       
    def r_scored(self):
        
        
        self.r_score += 1
    
        self.increase_score()
       

        
