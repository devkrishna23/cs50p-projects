text = input("Expression: ")

l = text.strip().split()

a = float(l[0])
ex = l[1]
b = float(l[2])

if ex == '+':
    print(a + b)
if ex == '-':
    print(a - b)
if ex == '*':
    print(a * b)
if ex == '/':
    print(a / b)