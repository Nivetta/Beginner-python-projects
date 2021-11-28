# importing all the classes from tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    
    # to cancel the timer loop when the reset button is clicked
    window.after_cancel(timer)
    # to reset the title, time and checkmarks to original state
    canvas.itemconfig(timer_text,text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    # to reset reps to zero to ensure start from the begining
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

#this function will be called when the start button is pressed
def start_timer():
    
    global reps
    reps+=1
    
    # countdown will be in minutes
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    if reps%2!=0:
        count_down(work_sec)
        title.config(text="WORK",fg=GREEN)
    elif reps==8: #try reps%8==0
        count_down(long_break_sec)
        title.config(text="LONG BREAK",fg=RED)
    else:
        count_down(short_break_sec)
        title.config(text="SHORT BREAK",fg=PINK)
         
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec= count%60
    
    # dynamic typing is used to format the output like 00:00
    if count_sec<10:
        count_sec = f"0{count_sec}"
        
    # to change  a canvas widget, use canvas.item.config(what_to_be_changed,changed_to)
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count>0:
        global timer
        #since we cant have 2 loops in a gui, we use the after method, 
        #parameters(time in ms, function to be called,parameters to function)
        timer = window.after(1000,count_down,count-1)
        
    else:
        
        # to trigger the function again so that a break is displayed after 1 rep
        start_timer()
        
        # to add a checkmark everytime a rep is comlpeted
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg=YELLOW )

# the dimensions are in pixels
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file="C:\\Users\\nivet\\100daysofcode\\Tkinter\\tomato.png")

# placing the image in the middle of the window
canvas.create_image(102 ,112,image = tomato_img)

# putting text on top of the image, at its centre
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row =1, column = 2 )

# creating the timer label
title = Label(text="Timer",font=(FONT_NAME,40,"bold"),bg=YELLOW,fg="green")
title.grid(row = 0, column=2)

#creating the start button, highlightthickness changes the space around the button to assigned number
start_button = Button(text="Start",highlightthickness=0,bg=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)

# creating the reset button
Reset_button = Button(text="Reset",highlightthickness=0,bg=YELLOW,command = reset_timer)
Reset_button.grid(row=2,column=3)

# creating the checkmark label
check_marks = Label(fg="green",bg=YELLOW,font=(30))
check_marks.grid(row=3,column=2)



# Event driven, checks if something happens on the screen all the time
window.mainloop()