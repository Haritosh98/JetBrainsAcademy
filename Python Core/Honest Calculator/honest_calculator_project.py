from operator import add, sub, mul, truediv

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
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"


def is_one_digit(v):
    if v % 1 == 0 and -10 < v < 10:
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v=v1) and is_one_digit(v=v3):
        msg = msg + msg_6  # "" + "... lazy" = "... lazy"
        if (v1 == 1 or v3 == 1) and v2 == '*':
            msg = msg + msg_7  # "" + "... very lazy" = "... lazy"
            if (v1 == 0 or v3 == 0) and (v2 in '*+-'):
                msg = msg + msg_8  # "" + "... very, very lazy" = "... very, very lazy"
        elif (v1 == 0 or v3 == 0) and (v2 in '*+-'):
            msg = msg + msg_8  # "" + "... very, very lazy" = "... very, very lazy"
    elif (v1 == 0 or v3 == 0) and (v2 in '*+-'):
        msg = msg + msg_8  # "" + "... very, very lazy" = "... very, very lazy"
    if msg != "":
        msg = msg_9 + msg  # "You are" +
        return msg
    else:
        return None

	
memory = 0.0
opers = {'+': add, '-': sub, '*': mul, '/': truediv}
while True:
    x, op, y = input("Enter an equation\n").split(' ')
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        if op in '+-*/':
            if check(v1=x, v2=op, v3=y) is not None:
                print(check(v1=x, v2=op, v3=y))
            try:
                result = opers[op](float(x), float(y))
                print(result)
            except ZeroDivisionError:
                print("Yeah... division by zero. Smart move...")
                continue
            store = input("Do you want to store the result? (y / n):\n")
            if store == 'y':
                if is_one_digit(v=result) is True:
                    message_10 = input(msg_10)
                    if message_10 == 'y':
                        message_11 = input(msg_11)
                        if  message_11 == 'y':
                            message_12 = input(msg_12)
                            if message_12 == 'y':
                                memory = result
                else:
                    memory = result # elif message_10 == 'n' or message_11 == 'n' or message_12 == 'no':
            if input("Do you want to continue calculations? (y / n):\n") == "n":   # only works with if and not elif
                break
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
