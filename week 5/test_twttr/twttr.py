def main():
    word = input("Input: ")
    new_word  = shorten(word)
    print(f"Output: {new_word}")


def shorten(word):
    new_word = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in word:
        if i not in vowels:
            new_word += i
    return new_word


if __name__ == "__main__":
    main()