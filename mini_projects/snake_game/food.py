from turtle import Turtle
import random


FOOD_TYPE = "turtle"
class Food(Turtle):

    def __init__(self, food_color):
        super().__init__()
        self.shape(FOOD_TYPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(food_color)
        self.speed("fastest")
        self.refresh()

        
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
