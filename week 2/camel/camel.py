camel = input("camelCase: ")
snake = ""


for c in camel:
    if not c.isupper():
        snake += c
    else:
        snake += '_' + c

print(f"snake_case: {snake.lower()}")