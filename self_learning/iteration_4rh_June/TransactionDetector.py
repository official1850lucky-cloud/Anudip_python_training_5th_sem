# Program to input transaction amounts continuously.
# Stop when -1 is entered.
# Count transactions above ₹50,000, below ₹1,000,
# and calculate the total transaction amount.
print("----- Transaction Analysis -----")
above_50000 = 0      # Counter for transactions above 50000
below_1000 = 0       # Counter for transactions below 1000
total_amount = 0     # Sum of all transaction amounts
while True:
    amount = float(input("Enter transaction amount (-1 to stop): "))
    # Stop the loop if user enters -1
    if amount == -1:
        break
    # Add amount to total
    total_amount += amount
    # Check transaction categories
    if amount > 50000:
        above_50000 += 1
    if amount < 1000:
        below_1000 += 1
# Display results
print("\n----- Transaction Summary -----")
print("Transactions above ₹50,000 :", above_50000)
print("Transactions below ₹1,000  :", below_1000)
print("Total Transaction Amount   : ₹", total_amount)
