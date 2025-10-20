import inflect

engine = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except (KeyboardInterrupt, EOFError):
        break
print(f"\nAdieu, adieu, to {engine.join(names)}")