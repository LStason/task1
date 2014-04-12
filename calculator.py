def convert_to_list(s):
    i = 0
    sign = 0
    a = []
    while i < len(s):
        if s[i].isdigit() == 1:
            if sign == 1:
                temp = '-'
                sign = 0
                temp += s[i]
            else:
                temp = s[i]
            j = i + 1
            while j < len(s) and (s[j].isdigit() == 1 or s[j] == '.'):
                temp += s[j]
                i += 1
                j += 1
            a.append(float(temp))
            i += 1
        elif s[i] == '-' and (i == 0 or s[i-1] == '('):
            sign = 1
            i += 1
        else:
            a.append(s[i])
            i += 1
    return a

def priority(a, b):
    if (a == '+' or a == '-') and (b == '*' or b == '/' or b == '+' or b == '-'):
        return 0
    else:
        return 1

def convert_to_postfix(a):
    b = []
    stack = []
    for x in a:
        if type(x) == float:
            b.append(x)
        elif x == '-' or x == '+' or x == '*' or x == '/':
            if len(stack) == 0:
                stack.append(x)
            else:
                while len(stack) > 0 and priority(x, stack[-1]) == 0:
                    b.append(stack.pop())
                stack.append(x)
        elif x == '*' or x == '/':
            stack.append(x)
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack[-1] != '(':
                b.append(stack.pop())
            stack.pop()
    while len(stack) > 0:
        b.append(stack.pop())
    return b

def operation(b, a, operand):
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*':
        return a * b
    elif operand == '/':
        return a / b

def calculation(s):
    s = s.replace(' ', '')
    b = convert_to_list(s)
    a = convert_to_postfix(b)
    stack = []
    for x in a:
        if type(x) == float:
            stack.append(x)
        else:
            stack.append(operation(stack.pop(), stack.pop(), x))
    return stack[-1]

string = raw_input("Input string: ")
print(calculation(string))