def main():

    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            print(gauge(percentage))
            break
        

def convert(fraction):

    a,b = fraction.split('/')
    if not (a.isdigit() and b.isdigit()):
        raise ValueError
    else:
        a = int(a)
        b = int(b)
        if b == 0:
            raise ZeroDivisionError
        elif a > b:
            raise ValueError
        else:
            return round((a / b) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()