text = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

if text.strip() == "42" or text.lower() == "forty-two" or text.lower() == "forty two":
    print("Yes")
else:
    print("No")