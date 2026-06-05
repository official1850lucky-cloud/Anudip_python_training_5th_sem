# contentGiven an amount, determine the minimum number of notes required using: ₹500, ₹200, ₹100, ₹50, ₹20, ₹10
amount = int(input("Enter amount: "))
# Array collection tracking our denominations
denominations = [500, 200, 100, 50, 20, 10]
print("Output:")
for note in denominations:
    if amount >= note:
        count = amount // note  # Integer division to find note quantity
        amount = amount % note  # Modulo to get remaining balance change
        print(f"{note} x {count}")