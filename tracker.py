import csv

def search_expense():
    query = input("Enter item name to search: ").lower()
    found = False
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and query in row[0].lower():
                print(f"🔍 Found: {row[0]} - ₹{row[1]}")
                found = True
    if not found:
        print("Empty search. No matching items.")
        
def show_total_expenses():
    total = 0
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row: # Make sure the row isn't empty
                    try:
                        # Change [0] to [1] to target the AMOUNT column
                        total += float(row[1]) 
                    except ValueError:
                        # This skips the header or any non-number rows
                        continue 
        print(f"💰 Total Spending to Date: ₹{total:.2f}")
    except FileNotFoundError:
        print("❌ No expense file found yet.")

# --- WRITER BLOCK ---
with open("expenses.csv", "a", newline="") as file:
    writer = csv.writer(file)
    while True:
        item = input("Enter item (or 'exit' or 'search' or 'total'): ").strip()
        
        if item.lower() == 'exit':
            break
        elif item.lower() == 'search':
            search_expense()
        elif item.lower() == 'total':
            show_total_expenses()
            continue # Go back to the start of the loop
            
        amount = input(f"Enter amount: ")
        writer.writerow([item, amount])
        print(f"Logged: {item}-{amount}")

print("Session closed.")