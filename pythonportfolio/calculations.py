def calculate(args):
    c = None
    for i in range(len(args)):
        if args[i][0] == "":
            break
        elif args[i][0] == "+":
            c = float(args[i][1]) + float(args[i][2])
            args[i+1][1] = c
        elif args[i][0] == "-":
            c = float(args[i][1]) - float(args[i][2])
            args[i+1][1] = c
        elif args[i][0] == "*":
            c = float(args[i][1]) * float(args[i][2])
            args[i+1][1] = c
        elif args[i][0] == "/":
            c = float(args[i][1]) / float(args[i][2])
            args[i+1][1] = c
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
            args[numArgs][2] = args[numArgs][2] + char
            args[numArgs + 1][1] = args[numArgs + 1][1] + char
            if dataType != "num":
                numArgs += 1
                dataType = "num"
        elif(char in ["+", "-", "*", "/"]):
            firstNum = False;
            args[numArgs][0] = args[numArgs][0] + char
            dataType = "op"
        elif(char == " "):
            continue
        else:
            print("Not Valid")
            args = []
            break
    return args

def run():
    command = input("What is your calculation?")
    args = parseArg(command)
    ans = calculate(args)
    print(ans)
    run()


run()