from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
# Turning of the animation, so the snake moves as a whole
screen.tracer(0)


# setting up the screen
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

# object creation
snake = Snake()
food = Food()
score = Scoreboard()

# calls the respective functions when buttons are pressed
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

# this loop makes the snake automatically move
game_on = True
while game_on:
    
    # since tracer method is used, we need to update changes to screen for it to be visible
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    # Detect collision with walls
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() >290 or snake.head.ycor() >290:
        game_on = False
        score.game_over()
        
    # Detect collision with tail
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
        
screen.exitonclick()


