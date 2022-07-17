msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
sign = ['-', '+', '*', '/']
result = 0

while True:
    print(msg_0)
    x, oper, y = input().split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in sign:
        print(msg_2)
        continue

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        if y == 0:
            print(msg_3)
            continue
        else:
            result = x / y

    print(result)

    break


