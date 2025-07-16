from turtle import Turtle
import random

SHAPE = "circle"
COLORS = ["blue","orange","yellow","pink","magenta","aquamarine"]

class Food(Turtle) :
    #Renders itself as a circle in the screen
    def __init__ (self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()

    def refresh(self) :
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)