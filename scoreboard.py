from turtle import Turtle

FONT = ("Courier", 24, 'normal')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()















        



