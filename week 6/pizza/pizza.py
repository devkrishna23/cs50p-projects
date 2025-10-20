import csv, sys
from tabulate import tabulate

n = len(sys.argv)

if n > 2:
    sys.exit("Too many command-line arguments")
elif n < 2:
    sys.exit("Too few command-line arguments")
else:
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        print("Not a csv file")
        sys.exit(1)
    else:
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                table = tabulate(reader, headers="keys" ,tablefmt="grid")
                print(table)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
    