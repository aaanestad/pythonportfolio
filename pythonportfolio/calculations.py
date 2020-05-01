def calculate(args):
    c = None
    for i in range(len(args)):
        if args[i][1] == "":
            break
        elif args[i][1] == "+":
            c = float(args[i][2]) + float(args[i+1][3])
        elif args[i][1] == "-":
            c = float(args[i][2]) - float(args[i+1][3])
        elif args[i][1] == "*":
            c = float(args[i][2]) * float(args[i+1][3])
        elif args[i][1] == "/":
            c = float(args[i][2]) / float(args[i+1][3])
    return c

def parseArg(s):
    args = [5*["", "", ""]]
    numArgs = 0
    dataType = "op"
    for char in s:
        if((char.isdigit() or char == ".") and numArgs == 0):
            args[numArgs][2] = args[numArgs][2] + char
        elif(char.isdigit() or char == "."):
            dataType == "number"
            args[numArgs][3] = args[numArgs][3] + char
            args[numArgs + 1][2] = args[numArgs + 1][2] + char
        elif(char in ["+", "-", "*", "/"]):
            if dataType != "op":
                numArgs += 1
                dataType = "op"
            args[numArgs][1] = args[numArgs][1] + char
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
