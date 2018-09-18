from tkinter import *
def doNothing():
    print("okay, I won't")
    
root = Tk()

menu = Menu(root)                       #Menu pre defined
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File",menu = subMenu)
subMenu.add_command(label="New Project", command = doNothing)
subMenu.add_command(label="New ...", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command = doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu = editMenu)
editMenu.add_radiobutton(label="redo",command = doNothing)

root.mainloop()