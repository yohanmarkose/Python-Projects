from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    

    def __init__(self, snake_color):
        """
        Args:
            snake_color (string): specify the color of snake. eg: "white", "blue" etc.
            refer color attribute in turtles module
        """
        self.segments = []
        self.snake_color = snake_color
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)
            
    
    def add_segment(self, pos):
        self.snake_body = Turtle(shape="square")
        self.snake_body.color(self.snake_color)
        self.snake_body.penup()
        self.snake_body.goto(pos)
        self.segments.append(self.snake_body)

    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # each segment will move towards wherever the seg in front of it is
        self.head.forward(PACE)

    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
