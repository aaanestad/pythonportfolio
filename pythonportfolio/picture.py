from tkinter import *
import calculations

gui = Tk()
btn = Button(gui, text="click me") #command = calculations.run()
btn.pack()
gui.wm_geometry("500x500")
gui.mainloop()
