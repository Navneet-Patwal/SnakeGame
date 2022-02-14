from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DIS = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)



    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.head.fd(MOVING_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)