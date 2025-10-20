import sys


n = len(sys.argv)

if n > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif n < 2:
    print("Too few command-line arguments")
    sys.exit(1)

filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a python file")

try:
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File not found")