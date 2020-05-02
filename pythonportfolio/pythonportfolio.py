def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def add(a, b):
    return float(a) + float(b)

def subtract(a, b):
    return float(a) - float(b)

def multiply(a, b):
    return float(a) * float(b)

def divide(a, b):
    return float(a) / float(b)

def run():
    print("Operations: +, -, *, /")
    command = input("Type calculation with spaces: ")
    arguments = command.split(" ")
    secondArg = False;
    for argument in arguments:
        if secondArg == True:
            if is_number(argument):
                b = float(argument)
                break
            if argument in ["+", "-", "*", "/"]:
                op = argument
            else:
                print("Not Valid Input")
                run()
                return
        if secondArg == False:
            if is_number(argument):
                a = float(argument)
                secondArg = True
            else:
                print("Not Valid Input")
                run()
                return
    if op == "+":
        c = add(a, b)
    if op == "-":
        c = subtract(a, b)
    if op == "*":
        c = multiply(a, b)
    if op == "/":
        c = divide(a, b)
    print(c)
    run()

#run()
