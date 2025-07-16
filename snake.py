from turtle import  Screen, Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self, size, pixel_size,speed):
        self.size = size
        self.pixel_size = pixel_size
        self.snake = []
        self.speed = speed
        self.create_snake()
        self.head = self.snake[0]

    # Configures the initial snake
    def create_snake(self):
        for i in range(0, self.size):
            new_pixel = Turtle()
            new_pixel.color("white")
            new_pixel.shape("square")
            new_pixel.speed(1)
            new_pixel.penup()
            new_pixel.setx(-i * self.pixel_size)
            self.snake.append(new_pixel)

    def move(self):
        for pixel in range (len(self.snake)-1,0,-1) :
            new_x = self.snake[pixel-1].xcor()
            new_y = self.snake[pixel-1].ycor()
            self.snake[pixel].goto(new_x,new_y)
        self.head.forward(self.speed)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

