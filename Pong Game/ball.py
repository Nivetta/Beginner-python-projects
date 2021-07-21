from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # All objects of the ball class is initialised with the following properties
        self.shape("circle")
        self.color("purple")
        self.shapesize(1,1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x,new_y )
        
    def bounce_y(self):
        # Reversing the direction of ball movement in y-axis
        self.y_move *= -1
        
    def bounce_x(self):
        # Reversing the direction of ball movement in x-axis
        self.x_move *= -1
        
    def refresh(self):
        self.goto(0,0)
        # If one player misses, ball goes to other player
        self.bounce_x()
        
        