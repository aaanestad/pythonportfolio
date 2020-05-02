from tkinter import *
import calculations

gui = Tk()
btn = Button(gui, text="Enter", command = calculations.run, height=4, width=8)
btn.grid(row = 4, column = 2)

oneBtn = Button(gui, text = "1", height=4, width=8, bg='orange', command=calculations.makeString("1"))
twoBtn = Button(gui, text = "2", height=4, width=8, bg='orange', command=calculations.makeString("2"))
threeBtn = Button(gui, text = "3", height=4, width=8, bg='orange', command=calculations.makeString("3"))
fourBtn = Button(gui, text = "4", height=4, width=8, bg='orange', command=calculations.makeString("4"))
fiveBtn = Button(gui, text = "5", height=4, width=8, bg='orange', command=calculations.makeString("5"))
sixBtn = Button(gui, text = "6", height=4, width=8, bg='orange', command=calculations.makeString("6"))
sevenBtn = Button(gui, text = "7", height=4, width=8, bg='orange', command=calculations.makeString("7"))
eightBtn = Button(gui, text = "8", height=4, width=8, bg='orange', command=calculations.makeString("8"))
nineBtn = Button(gui, text = "9", height=4, width=8, bg='orange', command=calculations.makeString("9"))
oneBtn.grid(row = 1, column = 0)
twoBtn.grid(row = 1, column = 1)
threeBtn.grid(row = 1, column = 2)
fourBtn.grid(row = 2, column = 0)
fiveBtn.grid(row = 2, column = 1)
sixBtn.grid(row = 2, column = 2)
sevenBtn.grid(row = 3, column = 0)
eightBtn.grid(row = 3, column = 1)
nineBtn.grid(row = 3, column = 2)

plusBtn = Button(gui, text = "+", height=4, width=8, bg='gray', command=calculations.makeString("+"))
minusBtn = Button(gui, text = "-", height=4, width=8, bg='gray', command=calculations.makeString("-"))
multBtn = Button(gui, text = "*", height=4, width=8, bg='gray', command=calculations.makeString("*"))
divBtn = Button(gui, text = "/", height=4, width=8, bg='gray', command=calculations.makeString("/"))
plusBtn.grid(row = 1, column = 3)
minusBtn.grid(row = 2, column = 3)
multBtn.grid(row = 3, column = 3)
divBtn.grid(row = 4, column = 3)

gui.wm_geometry("500x500")
gui.mainloop()
