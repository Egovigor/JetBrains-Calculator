msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
sign = ['-', '+', '*', '/']
result = 0
memory = 0.0

while True:
    print(msg_0)
    x, oper, y = input().split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

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

    while True:
        answer = input(msg_4)
        if answer == 'y':
            memory = result
            break
        elif answer == 'n':
            break
        else:
            continue

    start = False
    while True:
        answer = input(msg_5)
        if answer == 'y':
            start = True
            break
        elif answer == 'n':
            break
        else:
            continue

    if start:
        continue
    break


