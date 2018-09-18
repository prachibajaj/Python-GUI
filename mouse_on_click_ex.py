from tkinter import *

root = Tk()

def leftclick(event):
    print("Left")
def middleclick(event):
    print("Middle")
def rightclick(event):
    print("Right")
    
frame = Frame(root, width = 300,height = 200)
#Event is something the user does to the widget,function that gets called
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",middleclick)
frame.bind("<Button-3>",rightclick)
frame.pack()

root.mainloop()    