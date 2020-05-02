from tkinter import *

class mainCom():
    def __init__ (self):
        calcTime = " "

    def makeString(self, char):
        calcTime = str(char) + calcTime
        print("newchar = " + calcTime)

def run():
    print("pussy")
    print(com)
    args = parseArg(com)
    ans = calculate(args)
    print(ans)
    return

def calculate(args):
    c = None
    priority = []
    for e in reversed(args):
        if e[0] == "":
            priority.insert(0, e)
    for e in reversed(args):
        if e[0] == "+" or e[0]== "-":
            priority.insert(0, e)
    for e in reversed(args):
        if e[0] == "*" or e[0]== "/":
            priority.insert(0, e)
    for a in priority:
        i = args.index(a)
        if args[i][0] == "":
            break
        elif args[i][0] == "+":
            c = float(args[i][1]) + float(args[i][2])
            args[i+1][1] = float(c)
            args[i-1][2] = float(c)
        elif args[i][0] == "-":
            c = float(args[i][1]) - float(args[i][2])
            args[i+1][1] = float(c)
            args[i-1][2] = float(c)
        elif args[i][0] == "*":
            c = float(args[i][1]) * float(args[i][2])
            args[i+1][1] = float(c)
            args[i-1][2] = float(c)
        elif args[i][0] == "/":
            c = float(args[i][1]) / float(args[i][2])
            args[i+1][1] = float(c)
            args[i-1][2] = float(c)
    return c

def parseArg(s):
    args = [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]]
    numArgs = 0
    firstNum = True
    dataType = "num"
    for char in s:
        if((char.isdigit() or char == ".") and firstNum == True):
            args[numArgs][1] = args[numArgs][1] + char
        elif(char.isdigit() or char == "."):
            args[numArgs-1][2] = args[numArgs-1][2] + char
            args[numArgs][1] = args[numArgs][1] + char
        elif(char in ["+", "-", "*", "/"]):
            firstNum = False;
            args[numArgs][0] = args[numArgs][0] + char
            numArgs += 1
        elif(char == " "):
            continue
        else:
            print("Not Valid")
            args = []
            break
    return args

com = mainCom()
gui = Tk()
btn = Button(gui, text="Enter", command=lambda: run(), height=4, width=8)
btn.grid(row = 4, column = 2)

oneBtn = Button(gui, text = "1", height=4, width=8, bg='orange', command=lambda: com.makeString("1"))
twoBtn = Button(gui, text = "2", height=4, width=8, bg='orange', command=lambda: com.makeString("2"))
threeBtn = Button(gui, text = "3", height=4, width=8, bg='orange', command=lambda: com.makeString("3"))
fourBtn = Button(gui, text = "4", height=4, width=8, bg='orange', command=lambda: com.makeString("4"))
fiveBtn = Button(gui, text = "5", height=4, width=8, bg='orange', command=lambda: com.makeString("5"))
sixBtn = Button(gui, text = "6", height=4, width=8, bg='orange', command=lambda: com.makeString("6"))
sevenBtn = Button(gui, text = "7", height=4, width=8, bg='orange', command=lambda: com.makeString("7"))
eightBtn = Button(gui, text = "8", height=4, width=8, bg='orange', command=lambda: com.makeString("8"))
nineBtn = Button(gui, text = "9", height=4, width=8, bg='orange', command=lambda: com.makeString("9"))
oneBtn.grid(row = 1, column = 0)
twoBtn.grid(row = 1, column = 1)
threeBtn.grid(row = 1, column = 2)
fourBtn.grid(row = 2, column = 0)
fiveBtn.grid(row = 2, column = 1)
sixBtn.grid(row = 2, column = 2)
sevenBtn.grid(row = 3, column = 0)
eightBtn.grid(row = 3, column = 1)
nineBtn.grid(row = 3, column = 2)

plusBtn = Button(gui, text = "+", height=4, width=8, bg='gray', command=lambda: com.makeString("+"))
minusBtn = Button(gui, text = "-", height=4, width=8, bg='gray', command=lambda: com.makeString("-"))
multBtn = Button(gui, text = "*", height=4, width=8, bg='gray', command=lambda: com.makeString("*"))
divBtn = Button(gui, text = "/", height=4, width=8, bg='gray', command=lambda: com.makeString("/"))
plusBtn.grid(row = 1, column = 3)
minusBtn.grid(row = 2, column = 3)
multBtn.grid(row = 3, column = 3)
divBtn.grid(row = 4, column = 3)

gui.wm_geometry("500x500")
gui.mainloop()
