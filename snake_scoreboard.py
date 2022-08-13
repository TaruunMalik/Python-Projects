from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0 
        self.color('white')
        self.penup()
        self.goto(0,268)
        self.write(f"Current Score: {self.score}", align='center',font=('Arial',20,'normal'))
        self.hideturtle()
        self.updating_score()

    def updating_score(self):
        self.write(f"Current Score: {self.score}", align='center',font=('Arial',20,'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.updating_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= 'center', font='Arial')