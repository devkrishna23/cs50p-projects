def main():
    text = input()
    print(convert(text))


def convert(s):
    s = s.replace(":)" , "🙂")
    s = s.replace(":(" , "🙁")
    return(s)

if __name__ == "__main__":
    main()