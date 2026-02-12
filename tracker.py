import csv

with open("expenses.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # EVERYTHING BELOW IS INSIDE THE 'WITH' BLOCK
    while True:
        item = input("Enter item (or 'exit'): ").strip()
        if item.lower() == 'exit':
            break
        amount = input(f"Enter amount: ")
        writer.writerow([item, amount])
        print(f"Logged: {item}-{amount}")

print("Session closed.") # This is outside, so the file is now closed.
