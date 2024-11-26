from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')

class Score_Board(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)

        with open("data.txt") as data:  # Getting current High score from data file
            self.high_score = int(data.read())

        self.score = 0
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:  # Updating the high score on the file
                 data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)
