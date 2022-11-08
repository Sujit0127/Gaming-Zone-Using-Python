# Import Required Library
from tkinter import *
import random
 
# Create Object
root = Tk()
 

root.geometry("500x500")
root.title("Rock Paper Scissor Game")
root.configure(bg="orange")
root.resizable(False,False)
 
# Computer Value
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
 
# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
 
# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
# If player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text = match_result)
    l1.config(text = "Rock            ")
    l3.config(text = c_v)
    button_disable()
 
# If player selected paper
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Paper           ")
    l3.config(text = c_v)
    button_disable()
 
# If player selected scissor
def isscissor():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Scissor         ")
    l3.config(text = c_v)
    button_disable()
 
# Add Labels, Frames and Button
Label(root,text = " * Rock Paper Scissor * ",font = "Cambria 20 bold",fg = "black",bg="white").pack(pady = 20)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text = "PLAYER             ",font = "Cambria 13 bold",bg="orange")
 
l2 = Label(frame,text = "VS             ",font = "Cambria 13 bold",bg="orange")
 
l3 = Label(frame, text = "COMPUTER", font = "Cambria 13 bold",bg="orange")
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
 
l4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(root)
frame1.pack()
frame1.configure(bg="orange")
 
b1 = Button(frame1, text = "ROCK",font = "Cambria 13 bold",bg="green",fg="white", width = 7,command = isrock)
 
canvas1 = Canvas(width=58, height=58, bg="white")
canvas1.pack()
canvas1.place(x=118,y=230)
photo1 = PhotoImage(file='C:\\Users\\maity\\OneDrive\\Documents\\PROJ - CS881 Project - III\\rock1.png')
canvas1.create_image(0,0, image=photo1, anchor=NW)

b2 = Button(frame1, text = "PAPER",font = "Cambria 13 bold",bg="navyblue",fg="white", width = 7,command = ispaper)

canvas2 = Canvas(width=58, height=58, bg="white")
canvas2.pack()
canvas2.place(x=218,y=230)
photo2 = PhotoImage(file='C:\\Users\\maity\\OneDrive\\Documents\\PROJ - CS881 Project - III\\paper1.png')
canvas2.create_image(0,0, image=photo2, anchor=NW)
 
b3 = Button(frame1, text = "SCISSOR",font ="Cambria 13 bold",bg="red",fg="white", width = 7,command = isscissor)
 
canvas3 = Canvas(width=58, height=58, bg="white")
canvas3.pack()
canvas3.place(x=318,y=230)
photo3 = PhotoImage(file='C:\\Users\\maity\\OneDrive\\Documents\\PROJ - CS881 Project - III\\scissors1.png')
canvas3.create_image(0,0, image=photo3, anchor=NW)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
 
btn=Button(root, text = "RESET GAME",font ="Cambria 13 bold", fg = "white",bg = "maroon", command = reset_game)
btn.pack(pady = 20)
btn.place(x=185,y=320)
 
btn = Button(root, text=" EXIT ",font="Cambria 14 bold",fg="white",bg="grey",command=lambda: root.destroy())
btn.pack(padx=20, pady=20)
btn.place(x=210,y=390)



root.mainloop()