from tkinter import *
from tkinter import ttk
from functools import partial


# creating login function
def login():
    # getting form data
    uname = username.get()
    pwd = password.get()

    # applying validation
    if uname=='' or pwd=='':
        message.set("Empty field!")
    else:
      if uname=="murdoc" and pwd=="1234":
       message.set("Login success :)")
      else:
       message.set("Wrong username or password! Try again.")

            
# creating window
window = Tk()
window.title("Enter your account")
window.geometry("300x150")
window.config(bg="#000000")

# declaring variable
global message;
global username
global password
username = StringVar()
password = StringVar()
message=StringVar()

# creating frames
frame_user = Frame(window, width=300, height=50)
frame_user.grid(row=0, column=0)

frame_password = Frame(window, width=300, height=50)
frame_password.grid(row=1, column=0)

frame_button = Frame(window, width=300, height=50)
frame_button.grid(row=2, column=0)


# creating labels
label_user = Label(frame_user, text="Insert user: ", width=13, height=2, justify=LEFT, anchor="w", padx=8)
label_user.place(x=0, y=0)

label_password = Label(frame_password, text="Insert password: ", width=13, height=2, justify=LEFT, anchor="w", padx=8)
label_password.place(x=0, y=0)

label_message = Label(window, text="",textvariable=message, width=43)
label_message.place(x=0,y=126)

# creating fields
user_field = Entry(frame_user, textvariable=username, fg="#b77db8")
user_field.place(x=115, y=9)

password_field = Entry(frame_password, textvariable=password, fg="#b77db8", show="*")
password_field.place(x=115, y=9)

# creating button
button = Button(frame_button, command=login, text="Enter", width=20, height=1, bg="#634f60", fg="#FFFFFF")
button.place(x=75, y=0)


window.mainloop()