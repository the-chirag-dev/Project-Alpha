import csv

def search_expense():
    # .lower() here ensures the search isn't case-sensitive
    query = input("Enter item name to search: ").strip().lower()
    found = False
    
    try:
        # FIX: Changed .txt to .csv to match your writer
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            print(f"\n--- Search Result for '{query}' ---")
            for row in reader:
                # Basic error handling: check if row has data
                if row and query in row[0].lower():
                    print(f"Item: {row[0]} | Cost: {row[1]}")
                    found = True
            
            if not found:
                print("No matching expenses found")
    except FileNotFoundError:
        print("No data file found yet. Add an expense first!")

# --- WRITER BLOCK ---
with open("expenses.csv", "a", newline="") as file:
    writer = csv.writer(file)
    while True:
        item = input("Enter item (or 'exit' or 'search'): ").strip()
        
        if item.lower() == 'exit':
            break
        elif item.lower() == 'search':
            search_expense()
            continue # Go back to the start of the loop
            
        amount = input(f"Enter amount: ")
        writer.writerow([item, amount])
        print(f"Logged: {item}-{amount}")

print("Session closed.")