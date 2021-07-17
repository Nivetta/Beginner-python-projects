from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
class Snake:
    def __init__(self):
        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]
    
    def create_snake(self):       
        # creating snake body
        for position in POSITIONS:
            self.add_segment(position)
            
            
    def add_segment(self,position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.my_snake.append(segment)
        
    def extend(self):
        self.add_segment(self.my_snake[-1].position())
        
        
    def move(self):
        # To make the snake body to follow the head
        for seg_num in range(len(self.my_snake)-1,0,-1):
            #switching the place of the first with second and so on
            new_x = self.my_snake[seg_num -1].xcor()
            new_y = self.my_snake[seg_num -1].ycor()
            self.my_snake[seg_num].goto(new_x,new_y)
        self.head.forward(20)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        