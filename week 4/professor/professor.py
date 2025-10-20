import random


def main():

    level = get_level()
    correct = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        actual = a + b
        wrong = 0
        while wrong < 3:
            try:
                sum_ = int(input(f"{a} + {b} = "))
                if sum_ == actual:
                    correct += 1
                    break
                else:
                    print("EEE")
                    wrong += 1
            except (ValueError):
                print("EEE")
                wrong += 1
        if wrong == 3:
            print(f"{a} + {b} = {actual}")
    print(f"Score: {correct }")



def get_level():
    num = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in num:
                break
        except (TypeError, ValueError):
            pass
    return level


def generate_integer(level):

    if level == 1:
        a = random.randint(0,9)
    elif level == 2:
        a = random.randint(10,99)
    elif level == 3:
        a = random.randint(100,999)
    return a

if __name__ == "__main__":
    main()