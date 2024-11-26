import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self, ball_color):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color(ball_color)
        self.displace_x = random.randint(2, 5)
        self.displace_y = random.randint(2, 5)
        self.move_speed = 0.02
        
    
    def move(self):
        new_y = self.ycor() + self.displace_y
        new_x = self.xcor() + self.displace_x
        self.goto(new_x, new_y)            


    def bounce_y(self):
        self.displace_y *= -1
    

    def bounce_x(self):
        self.displace_x *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.025
        self.displace_x *= -1
