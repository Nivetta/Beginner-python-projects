from turtle import Turtle
FONT = ("Arial",22,"normal")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white")
        self.penup()
        self.goto(0,267)
        self.hideturtle()
        self.update()
        
    def update(self):
        self.write(f"Score : {self.scores}",align=ALIGN,font=FONT)
        
    def increase_score(self):
        self.scores += 1
        self.clear()        
        self.update()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN,font=FONT)
        
        
        
        
    
        
        
        
        