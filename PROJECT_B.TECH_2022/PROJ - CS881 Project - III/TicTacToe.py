#import needed library
from tkinter import *
import random as r
#Function to define a button
def CellButton(frame):
    b=Button(frame,padx=1,bg="#27386B",width=3,text="   ",font=('algerian',60,'bold'),relief="sunken",bd=5)
    return b
#changing operator for the next player
def changeLetter():
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
#Reset the gameboard
def resetBoard():
    global a
    for i in range(3):
        for j in range(3):
                board[i][j]["text"]=" "
                board[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
#check for winning
def checkWinning():
    for i in range(3):
            if(board[i][0]["text"]==board[i][1]["text"]==board[i][2]["text"]==a or board[0][i]["text"]==board[1][i]["text"]==board[2][i]["text"]==a):
                if a == 'X':
                    lblMesage.config(text="'" + firstPlayer.get() + "' is Winner")
                else:
                    lblMesage.config(text="'" + secondPlayer.get() + "' is Winner")
                resetBoard()
    if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]==a or board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]==a):
        if a =='X':
         lblMesage.config(text="'"+firstPlayer.get()+"' is Winner")
        else:
            lblMesage.config(text="'" + secondPlayer.get() + "' is Winner")
        resetBoard()
    elif(board[0][0]["state"]==board[0][1]["state"]==board[0][2]["state"]==board[1][0]["state"]==board[1][1]["state"]==board[1][2]["state"]==board[2][0]["state"]==board[2][1]["state"]==board[2][2]["state"]==DISABLED):
        lblMesage.config(text="The match is Tied!")
        resetBoard()

def click(row,col):
        board[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        lblMesage.config(text="")
        checkWinning()
        changeLetter()
        if a=='X':
         label.config(text=firstPlayer.get()+"'s Chance")
        else:
         label.config(text=secondPlayer.get() + "'s Chance")

#Defining window
root=Tk()
#Setting title for window
root.title("Tic-Tac-Toe Game")
#setting width and height for game window
root.geometry("800x490")
#setting background color
root["bg"]="#03151C"
#declaring variables
firstPlayer=StringVar()
secondPlayer=StringVar()
#label for first player
Label(root,text="First Player [X]",bg="#03151C",fg="white",font=("Arial",15,"bold")).place(x=550,y=20)
#textbox for first player
Entry(root,font=("Arial",15,"bold"),textvariable=firstPlayer).place(x=550,y=55)
#label for second player
Label(root,text="Second Player [O]",bg="#03151C",fg="white",font=("Arial",15,"bold")).place(x=550,y=90)
#textbox for second player
Entry(root,font=("Arial",15,"bold"),textvariable=secondPlayer).place(x=550,y=125)
#label for displaying game result
lblMesage=Label(root,bg="#03151C",fg="yellow",font=("Arial",15,"bold"))
lblMesage.place(x=550,y=185)
#Defining Two operators
a=r.choice(['O','X'])
#setting color for operators
colour={'O':"yellow",'X':"white"}
#variable for creating board
board=[[],[],[]]
for i in range(3):
        for j in range(3):
                board[i].append(CellButton(root))
                board[i][j].config(command= lambda row=i,col=j:click(row,col))
                board[i][j].grid(row=i,column=j)
#label for displaying player's turn
label=Label(text="Welcome",font=('arial',15,'bold'),bg="#03151C",fg="white")
label.place(x=550,y=450)
#run Application
root.mainloop()