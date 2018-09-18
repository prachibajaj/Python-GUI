from tkinter import *

root = Tk()
#Frame is a rectangular area that contain other
topFrame = Frame(root)
topFrame.pack(side = BOTTOM)
bottomFrame = Frame(root)
bottomFrame.pack()

b1 = Button(topFrame,text = 'Button 1',fg = 'red')
b2 = Button(topFrame,text = 'Button 2',fg = 'blue')
b3 = Button(topFrame,text = 'Button 3',fg = "green")
b4 = Button(bottomFrame,text = 'Button 4',fg = 'purple')

#these buttons will be on top
b1.pack(side = LEFT) #place as left as possible
b2.pack(side = LEFT)
b3.pack(side = LEFT)

#button 4 is on the top as frame on top and button in bottom of frame
b4.pack ()   #bottom not making any difference
root.mainloop()