def main():
    
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"Amount: {amount}")


def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
         return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()