#Create snake OK
#Move the snake OK
#Control the snake OK
#Detect collision with food OK
#Detect collision with wall OK
#Detect collision with tail
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Play while game_on conditions are true
game_on = True


#Create the initial snake
snake = Snake(3,20,20)
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.right ,"Right")
screen.onkey(snake.left ,"Left")


while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        score.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280 :
        game_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

#Ends the program
screen.exitonclick()

