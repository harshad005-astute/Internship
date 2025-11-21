
stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "CEMENT": 150,
    "MICROSOFT": 320,
    "STEEL": 100
}

def stock_tracker():
    total_value = 0
    records = []

    print("Welcome to Simple Stock Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' to finish.\n")

    while True:
        stock = input("Enter stock symbol: ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found! Try again.\n")
            continue

        qty = input("Enter quantity: ")
        if not qty.isdigit():
            print("Please enter a valid number.\n")
            continue

        qty = int(qty)
        cost = qty * stock_prices[stock]
        total_value += cost

        records.append(f"{stock}, {qty}, {cost}")
        print(f"Added: {stock} × {qty} = {cost}\n")

    print("\n--- Summary ---")
    print("Total Investment Value:", total_value)
    save = input("Save results to file? (yes/no): ").lower()
    if save == "yes":
        filename = input("Enter filename (txt or csv): ")
        if filename.endswith(".txt"):
            with open(filename, "w") as f:
                f.write("Stock, Quantity, Value\n")
                for r in records:
                    f.write(r + "\n")
                f.write(f"Total Investment: {total_value}")
        elif filename.endswith(".csv"):
            with open(filename, "w") as f:
                f.write("Stock,Quantity,Value\n")
                for r in records:
                    f.write(r.replace(", ", ",") + "\n")
                f.write(f"TOTAL,,{total_value}")
        else:
            print("Invalid file type! Must be .txt or .csv")
        print("File saved successfully!")
stock_tracker()
