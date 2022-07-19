msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
sign = ['-', '+', '*', '/']
result = 0
memory = 0.0


def is_one_digit(v) -> bool:
    if v > -10 and v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)



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

    check(x, y, oper)

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
