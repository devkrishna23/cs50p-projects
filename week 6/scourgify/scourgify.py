import csv, sys

n = len(sys.argv)

if n < 3:
    sys.exit("Too few command-line arguments")
elif n > 3:
    sys.exit("Too many command-line arguments")
else:
    before = sys.argv[1]
    new = sys.argv[2]
    if not before.endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        try:
            with open(before, 'r') as file:
                reader = csv.DictReader(file)
                with open(new, 'w') as after:
                    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for line in reader:
                        last,first = line["name"].split(',')
                        house = line["house"]
                        first = first.strip()
                        last = last.strip()
                        writer.writerow({"first": first, "last": last, "house": house})
                
                sys.exit(0)
        except FileNotFoundError:
            sys.exit(f"Could not read {before}")