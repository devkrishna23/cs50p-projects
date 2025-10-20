total = 50
valid = [25, 10, 5]
change_total = 0

while total > 0 and change_total <= 50:
    print(f"Amount Due: {total}")
    change = int(input("Insert Coin: "))
    if change not in valid:
        pass
    else:
        total -= change
        change_total += change 

print(f"Change Owed: {abs(total)}")
