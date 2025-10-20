def main():
    plate = input("Plate: ")
    valid = is_valid(plate)
    if valid == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len(s)
    if not 2 <= n <= 6:
        return False
    else:
        if not (s[0].isalpha() or s[1].isalpha()):
            return False
        else:
            for char in s:
                if not (char.isalpha() or char.isdigit()):
                    return False
            index = -1
            for i in range(n):
                if s[i].isdigit():
                    index = i
                    break
            
            if index == -1:
                return True

            if s[index] == '0':
                return False

            for j in range(index, n):
                if not s[j].isdigit():
                    return False
            return True  


if __name__ == "__main__":
    main()