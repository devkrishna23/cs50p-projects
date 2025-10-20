text = input("Greeting: ")
text = text.lower().strip()

value = 0

if text.startswith("hello"):
    print("$0")
elif text.startswith('h'):
    print("$20")
else:
    print("$100")