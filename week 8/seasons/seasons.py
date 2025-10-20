from datetime import date
import inflect
import sys


def main():
    birth = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_lived(birth_date))


def minutes_lived(birth_date):
    today = date.today()
    delta = today - birth_date
    minutes = delta.days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"


if __name__ == "__main__":
    main()
