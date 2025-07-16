#Create snake
#Move the snake
#Control the snake
#Detect collision with food
#Detect collision with wall
#Detect collision with tail
from distutils.core import run_setup
from turtle import  Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600,600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


game_on = True



#Create the initial snake
snake = Snake(3,20,20)
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.right ,"Right")
screen.onkey(snake.left ,"Left")


while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()






#Ends the program
screen.exitonclick()

