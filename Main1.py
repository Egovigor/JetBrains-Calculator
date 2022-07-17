msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
sign = ['-', '+', '*', '/']

while True:
    print(msg_0)
    x, oper, y = input().split()

    try:
        float(x)
        float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in sign:
        print(msg_2)
        continue

    break
