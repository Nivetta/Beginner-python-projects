from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pwd():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_list = []
    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)
    
    password = "".join(password_list)
    pwd_entry.insert(0,password)
    # To automatically copy the password into the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
   
    website = website_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()
    
    # checking if any of the fields are empty
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Don't Leave Any Field Empty!")
    else:
        
    
        # showing a message box to confirm or cancel the entered details
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}"
                                       f"\nPassword : {password} \n Is it ok to save?")
        
        if is_ok:
            with open("data.txt","a") as file_obj:
                file_obj.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                pwd_entry.delete(0,END)
                                      
# ---------------------------- UI SETUP ------------------------------- #

# creating the window and setting the title
window = Tk()
window.title("Password Manager")
window.config(padx = 50,pady=50)

# creating the canvas
canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
lock_img = PhotoImage(file="C:\\Users\\nivet\\100daysofcode\\Tkinter\\logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(row = 0, column = 1)

# creating the website label
website_label = Label(text="Website ")
website_label.grid(row = 1, column = 0)

# creating entry box for website
website_entry = Entry(width=36)
website_entry.grid(sticky = N+E+W+S,row = 1, column = 1, columnspan =2)
# making cursor focus in the entry box
website_entry.focus()

# creating the Email Label
email_label = Label(text="Email/Username ")
email_label.grid(row = 2, column = 0)

# creating entry box for email
email_entry = Entry( width = 36 )
email_entry.grid( sticky = N+E+W+S ,row = 2, column = 1, columnspan =2)
# displaying the most commonly displayed email in the text box
email_entry.insert(0,"nivetta@gmail.com")

# creating the password label
pwd_label = Label(text="Password ")
pwd_label.grid(row = 3, column = 0)

# creating entry box for pwd
pwd_entry = Entry(width=21)
pwd_entry.grid( sticky = N+E+W+S , row = 3, column = 1)

# Creating Generate button
gen_button = Button(text="Generate Password",command=gen_pwd)
gen_button.grid( row = 3 , column = 2)

# Creating add button
add_button = Button( text="Add" , width=36 , command = save)
add_button.grid(sticky = N+E+W+S,row =4, column = 1, columnspan = 2)







window.mainloop()

