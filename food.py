from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        self.turtlesize(0.5,0.5)
        self.speed("fastest")
        self.goto(randint(-280,280),randint(-280,280))
        self.refresh()
    def refresh(self):
    
        self.goto(randint(-280,280),randint(-280,280))
        
        
        
        
        
        

