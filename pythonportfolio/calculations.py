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
    print(priority)
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
        print(args)
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

def run():
    command = input("What is your calculation? ")
    args = parseArg(command)
    ans = calculate(args)
    print(ans)
    run()

run()
