twitter = input("Input: ")
twttr = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for c in twitter:
    if c not in vowels:
        twttr += c
print(f"Output: {twttr}")