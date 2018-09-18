from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window title','Monkeys can live upto 300 years')
answer = tkinter.messagebox.askquestion("Do you like silly faces ?")

if answer == 'Yes':
      print("LOL")
      
root.mainloop()