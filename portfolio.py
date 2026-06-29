
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total = 0

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        amount = stocks[name] * qty
        total = total + amount
    else:
        print("Stock", name, "not available")

print("Total Investment Value =", total)