from tkinter import * 
import tkinter

def nextpage():
  root.destroy()
  import Menu_Page

root = Tk()
canvas = Canvas(width=1550, height=860, bg="black")
canvas.pack()
photo = PhotoImage(file="D:\Sujit's project\PROJECT_B.TECH_2022\PROJ - CS881 Project - III\\HomePage.png")
canvas.create_image(0,0, image=photo, anchor=NW)

btn = Button(root, text=" START NOW ",font="Cambria 14 bold",fg="white",bg="maroon",command=nextpage)
btn.pack(padx=25, pady=25)
btn.place(x=419,y=530)

btn = Button(root, text="CLOSE THE WINDOW",font="Cambria 14 bold",fg="white",bg="maroon",command=lambda: root.destroy())
btn.pack(padx=25, pady=25)
btn.place(x=387,y=630)

  
root.title("Home | Python Game Zone | Welcome")
#root.geometry("1280x720")
root.attributes('-fullscreen' , True)
#root.resizable(False,False)
root.configure(bg="light yellow")
mainloop()