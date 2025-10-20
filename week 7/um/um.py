import re

def main():
    print(count(input("Text: ")))

def count(s):
    
    pattern = r"\b(um)\b"
    search = re.findall(pattern, s, re.IGNORECASE)
    return len(search)



if __name__ == "__main__":
    main()