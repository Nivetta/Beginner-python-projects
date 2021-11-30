from tkinter import *

# creating a window and configuring it
window = Tk()
window.title("Converter")

# Action triggered when convert button is clicked
def calculate():
    miles = float(entry_1.get())
    km = round(miles*1.609)
    km_label.config(text=str(km))
    

lable_1 = Label(text="Miles")
lable_1.grid(row = 0, column = 2)

entry_1 = Entry(width =10)
entry_1.grid(row =0, column = 1)

lable_2 = Label(text="is equal to")
lable_2.grid(row = 1, column = 0)

km_label = Label()
km_label.grid(row =1, column = 1)

lable_3 = Label(text="Km")
lable_3.grid(row = 1, column = 2)

button = Button(text="Convert", command = calculate)
button.grid(row = 3, column = 1)









window.mainloop()


