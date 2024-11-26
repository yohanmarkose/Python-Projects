from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, paddle_color, initial_pos):
        super().__init__(shape="square")
        """takes in the paddle color and initial goto position of the paddle
        """
        self.paddle_color = paddle_color
        self.initial_pos = initial_pos
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color(self.paddle_color)
        self.goto(self.initial_pos)

    
    def move_up(self):
        if self.ycor() <= 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)


    def move_down(self):
        if self.ycor() >= -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y) 
