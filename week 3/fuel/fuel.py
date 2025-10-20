while True:
    try:
        fraction = input("Fraction: ")
        a,b = fraction.split('/')
        a = int(a)
        b = int(b)
        if a >= 0 and b >= 0:
            if a > b:
                print("Invalid Input")
                continue
            percentage = round((a/b) * 100)
            if percentage >= 99:
                print("F")
            elif percentage <=  1:
                print("E")
            else:
                print(f"{percentage}%")
            break
    except (ValueError, ZeroDivisionError):
        print("Invalid Input")