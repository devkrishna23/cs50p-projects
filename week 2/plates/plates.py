import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    pattern = r"^[A-Z]{2,6}$|[A-Z]{2,}[1-9][0-9]*$"
    return re.match(pattern, s) and 2 <= len(s) <= 6


if __name__ == "__main__":
    main()