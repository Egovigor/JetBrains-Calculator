msg = {0: "Enter an equation",
       1: "Do you even know what numbers are? Stay focused!",
       2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       3: "Yeah... division by zero. Smart move...",
       4: "Do you want to store the result?  y / n):",
       5: "Do you want to continue calculations?  y / n):",
       6: " ... lazy",
       7: " ... very lazy",
       8: " ... very, very lazy",
       9: "You are",
       10: "Are you sure? It is only one digit! (y / n)",
       11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
       12: "Last chance! Do you really want to embarrass yourself? (y / n)"}

sign = ['-', '+', '*', '/']
result = 0
memory = 0.0


def is_one_digit(v) -> bool:
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    message = ""
    if is_one_digit(v1) and is_one_digit(v2):
        message += msg[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        message += msg[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        message += msg[8]
    if message != "":
        message = msg[9] + message
        print(message)


while True:
    print(msg[0])
    x, oper, y = input().split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg[1])
        continue

    if oper not in sign:
        print(msg[2])
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
            print(msg[3])
            continue
        else:
            result = x / y

    print(result)

    while True:
        answer = input(msg[4])
        if answer == 'y':
        else:
            memory = result

        elif answer == 'n':
        break
    else:
        continue

start = False
while True:
    answer = input(msg[5])
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
