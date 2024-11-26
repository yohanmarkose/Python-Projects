from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1


    def r_point(self):
        self.r_score += 1


    def completed_game(self, max_score):
        self.goto(0, 0)
        self.color("grey")
        if self.r_score == max_score:
            message = "Game over! the right player won"
        if self.l_score == max_score:
            message = "Game over! the left player"
        self.write(message, align="center", font=("Courier", 30, "normal"))
