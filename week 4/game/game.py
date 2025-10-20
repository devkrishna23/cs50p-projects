import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except (TypeError, ValueError):
        pass
        
ranint = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            pass
        else:
            if guess > ranint:
                print("Too large!")
            elif guess < ranint:
                print("Too small!")
            else:
                print("Just right!")
                break
    except (ValueError, TypeError):
        pass