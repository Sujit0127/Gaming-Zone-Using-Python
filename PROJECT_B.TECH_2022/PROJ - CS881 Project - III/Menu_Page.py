from tkinter import *
import tkinter


window = tkinter.Tk()

def snake():
    #window.destroy()
    import snake

def flappybird():
    #window.destroy()
    import flappybird

def PacMan():
    #window.destroy()
    import PacMan

def RockPaperScissor():
    #window.destroy()
    import RockPaperScissor

def TicTacToe():
    #window.destroy()
    import TicTacToe

def BubbleSortVisual():
    #window.destroy()
   import BubbleSortVisual

def pong():
    #window.destroy()
   import pong

def Tiles():
    #window.destroy()
    import Tiles


def Game1():
  myLabel = Label(window,text="""Snake is a video game genre where the player manoeuvres a growing line that becomes a primary obstacle to itself. 
  The concept originated in the 1976 two-player arcade game Blockade from Gremlin Industries, and the ease of implementation has led to hundreds of versions for many platforms.""",font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack()
  myLabel.place(x=105,y=644)



def Game2():
  myLabel = Label(window,text="""Flappy Bird is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen, under his game development company .Gears.  The  game  is a side-scroller 
  where the player controls a bird, attempting to fly between columns of green pipes without hitting them.""",font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


def Game3():
  myLabel = Label(window,text="""     Pac-Man is a Japanese video game franchise created by Toru Iwatani but published,developed 
       and owned by Bandai Namco Entertainment.Entries have been developed by a wide array of other video game companies, including Midway Games, Atari and Mass Media, Inc. """,font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


def Game4():
  myLabel = Label(window,text="""   Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who 
  succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. """,font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


def Game5():
  myLabel = Label(window,text="""Pong is a two-dimensional sports game that simulates table tennis. The player controls an in-game paddle by moving it vertically across the left or right side of the screen. They can 
  compete against another player controlling a second paddle on the opposing side. Players use the paddles to hit a ball back and forth.""",font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


def Game6():
  myLabel = Label(window,text="""Rock Paper Scissors is a hand game originating from China, usually played between two people,in which each player simultaneously forms one of three shapes with an outstretched
   hand. These shapes are "rock", "paper", and "scissors".  """,font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


def Game7():
  myLabel = Label(window,text="""A sliding puzzle, sliding block puzzle,or sliding tile puzzle is a combination puzzle that challenges a player to slide (frequently flat) pieces along certain routes (usually on a board)
   to establish a certain end-configuration. The pieces to be moved may consist of simple shapes. """,font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


def Game8():
  myLabel = Label(window,text="""     Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in 
  the wrong order.The pass through the list is repeated until the list is sorted.  """,font="Cambria 12 bold",bg="white",fg="black")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


window.title("Main Menu")

canvas999= Canvas(width=1550, height=715 , bg ='black' )
canvas999.pack()
#canva9992.place(x=75, y=165)
photo999= PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\MenuPage.png")
canvas999.create_image(0,0, image=photo999, anchor=NW)


#lbl = Label(window, text=" * * * LIST OF GAMES * * * " , bg="BLUE", fg="White",font= ('Cambria 19 bold'))
#lbl.pack()

canvas1 = Canvas(width=100, height=100 , bg ='white' )
canvas1.pack()
canvas1.place(x=310, y=170)
photo1 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\HungrySnake.png")
canvas1.create_image(0,0, image=photo1, anchor=NW)

LL1 = Label(window, text=" Hungry Snake  ",font="Calibri 15 bold",fg="red3",bg="white")
LL1.pack()
LL1.place(x=298,y=142)

btn1 = Button(window, text="P L A Y" , command=snake)
btn1.pack(padx=20, pady=20)
btn1.place(x=265, y=280)
btn1.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'blue3' , fg = 'white' )

btn11 = Button(window, text="A B O U T" , command=Game1)
btn11.pack(padx=20, pady=20)
btn11.place(x=365, y=280)
btn11.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white' )


canvas2 = Canvas(width=100, height=100 , bg ='white' )
canvas2.pack()
canvas2.place(x=577, y=170)
photo2 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\FlappyBird.png")
canvas2.create_image(0,0, image=photo2, anchor=NW)

LL2 = Label(window, text=" Flappy Bird  ",font="Calibri 15 bold",fg="red3",bg="white")
LL2.pack()
LL2.place(x=573,y=152)

btn2 = Button(window, text="P L A Y" , command=flappybird )
btn2.pack(padx=20, pady=20)
btn2.place(x=534, y=280)
btn2.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'blue3' , fg = 'white')

btn22 = Button(window, text="A B O U T" , command=Game2)
btn22.pack(padx=20, pady=20)
btn22.place(x=634, y=280)
btn22.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')


canvas3 = Canvas(width=100, height=100 , bg ='white' )
canvas3.pack()
canvas3.place(x=875, y=170)
photo3 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\PacMan.png")
canvas3.create_image(0,0, image=photo3, anchor=NW)

LL3 = Label(window, text=" Pac - Man  ",font="Calibri 15 bold",fg="red3",bg="white")
LL3.pack()
LL3.place(x=876,y=142)

btn3 = Button(window, text="P L A Y" , command=PacMan)
btn3.pack(padx=20, pady=20)
btn3.place(x=830, y=280)
btn3.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'BLUE3' , fg = 'white')

btn33 = Button(window, text="A B O U T", command=Game3)
btn33.pack(padx=20, pady=20)
btn33.place(x=930, y=280)
btn33.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')


canvas7 = Canvas(width=100, height=100 , bg ='white' )
canvas7.pack()
canvas7.place(x=1135, y=170)
photo7 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\SlidingPuzzle.png")
canvas7.create_image(0,0, image=photo7, anchor=NW)

LL7 = Label(window, text=" Sliding Puzzle ",font="Calibri 15 bold",fg="red3",bg="white")
LL7.pack()
LL7.place(x=1120,y=142)

btn7 = Button(window, text="P L A Y" , command=Tiles )
btn7.pack(padx=20, pady=20)
btn7.place(x=1090, y=280)
btn7.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'BLUE3' , fg = 'white')

btn77 = Button(window, text="A B O U T", command=Game7)
btn77.pack(padx=20, pady=20)
btn77.place(x=1190, y=280)
btn77.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')


#EXIT
btn99 = Button(window,height=2 , width =12,text="E X I T", font = 'Aerial 12 bold' ,bg = 'aquamarine2',fg = 'black',command=lambda:window.destroy(), border = '10')
btn99.pack()
btn99.place(x=710, y=730)

#clear

def clear():
  myLabel = Label(window,text=""" !!! Clear by DS !!!  Clear by DS !!! Clear by DS !!! Clear by DS !!! Clear by DS !!! Clear by DS !!! Clear by DS !!! Clear by DS !!!Clear by DS !!! Clear by DS !!! Clear by DS !!!
  !!! Clear by DS !!! Clear by DS !!! Clear by DS !!! Clear by DS !!!Clear by DS !!!Clear by DS !!!Clear by DS !!! .""",font="Cambria 12 bold",bg="#41c5a7",fg="#41c5a7")
  myLabel.pack(padx=20, pady=20)
  myLabel.place(x=105,y=644)


btn999 = Button(window,height=1 , width =8,text="C L E A R", font = 'Aerial 12 bold' ,bg = 'black',fg = 'gold',  command=clear)
btn999.pack()
btn999.place(x=732, y=607)


canvas4 = Canvas(width=100, height=100 , bg ='white' )
canvas4.pack()
canvas4.place(x=310, y=389)
photo4 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\TicTacToe.png")
canvas4.create_image(0,0, image=photo4, anchor=NW)

LL4 = Label(window, text=" Tic-Tac-Toe  ",font="Calibri 15 bold",fg="red3",bg="white")
LL4.pack()
LL4.place(x=305,y=360)

btn4 = Button(window, text="P L A Y" , command=TicTacToe )
btn4.pack(padx=20, pady=20)
btn4.place(x=265, y=503)
btn4.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'BLUE3', fg = 'white')

btn44 = Button(window, text="A B O U T", command=Game4)
btn44.pack(padx=20, pady=20)
btn44.place(x=365, y=503)
btn44.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')


canvas5 = Canvas(width=100, height=100 , bg ='white' )
canvas5.pack()
canvas5.place(x=577, y=389)
photo5 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\Pong.png")
canvas5.create_image(0,0, image=photo5, anchor=NW)

LL5 = Label(window, text=" Pong  ",font="Calibri 15 bold",fg="red3",bg="white")
LL5.pack()
LL5.place(x=595,y=360)

btn5 = Button(window, text="P L A Y", command=pong )
btn5.pack(padx=20, pady=20)
btn5.place(x=536, y=503)
btn5.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'BLUE3', fg = 'white')

btn55 = Button(window, text="A B O U T", command=Game5)
btn55.pack(padx=20, pady=20)
btn55.place(x=634, y=503)
btn55.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')


canvas6 = Canvas(width=100, height=100 , bg ='white' )
canvas6.pack()
canvas6.place(x=875, y=389)
photo6 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\RockPaperScissors.png")
canvas6.create_image(0,0, image=photo6, anchor=NW)

LL6 = Label(window, text=" Rock Paper Scissors  ",font="Calibri 15 bold",fg="red3",bg="white")
LL6.pack()
LL6.place(x=835,y=360)

btn6 = Button(window, text="P L A Y" , command=RockPaperScissor )
btn6.pack(padx=20, pady=20)
btn6.place(x=830, y=503)
btn6.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'blue3', fg = 'white')

btn66 = Button(window, text="A B O U T", command=Game6)
btn66.pack(padx=20, pady=20)
btn66.place(x=930, y=503)
btn66.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')


canvas8 = Canvas(width=100, height=100 , bg ='white' )
canvas8.pack()
canvas8.place(x=1135, y=389)
photo8 = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\BubbleSortVisual.png")
canvas8.create_image(0,0, image=photo8, anchor=NW)

LL8 = Label(window, text=" Bubble Sort Visual ",font="Calibri 15 bold",fg="red3",bg="white")
LL8.pack()
LL8.place(x=1102,y=360)

btn8 = Button(window, text="P L A Y" , command=BubbleSortVisual)
btn8.pack(padx=20, pady=20)
btn8.place(x=1090, y=503)
btn8.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'BLUE3' , fg = 'white')

btn88 = Button(window, text="A B O U T", command=Game8)
btn88.pack(padx=20, pady=20)
btn88.place(x=1190, y=503)
btn88.configure(height=2 , width =8, font = 'Aerial 12 bold italic' , bg = 'green4' , fg = 'white')

#Developed By

lbl = Label(window, text="Developed By",font="Calibri 13 bold italic",bg="light yellow",fg="black")
lbl.pack()
lbl.place(x=731,y=807)
lbl = Label(window, text=" DEBARATHI SARDAR | BITTU DEY | SUJIT MAITY ",font="Calibri 13 bold",bg="light yellow",fg="black")
lbl.pack()
lbl.place(x=604,y=830)


window.configure(bg='light yellow')

#window.resizable(False , False)

window.attributes('-fullscreen' , True)

#window.geometry("635x610")

window.mainloop()