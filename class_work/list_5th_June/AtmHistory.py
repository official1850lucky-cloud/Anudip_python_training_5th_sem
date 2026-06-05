#Write a program toCalculate the current balance, Count total deposits and withdrawals, Find the largest deposit and largest withdrawal and separate lists for deposits and withdrawals.  
transactions = [5000, -2000, 3000, -1000, -500, 7000] 
# Variables ko initialize kiya [cite: 23, 24, 26]
current_balance = 0
total_deposits = 0
total_withdrawals = 0
deposits = []
withdrawals = []
# Loop chalakar transactions check karenge
for t in transactions:
    # 1. Current balance calculate 
    current_balance += t
    # Positive then Deposit, Negative then Withdrawal 
    if t > 0:
        deposits.append(t) # add
        total_deposits += 1 # Count 
    else:
        withdrawals.append(t) # add 
        total_withdrawals += 1 # Count  
# Deposits list ke pehle element ko largest mana
largest_deposit = deposits[0]
for d in deposits:
    if d > largest_deposit:
        largest_deposit = d
# for largest withdrawl
largest_withdrawal = withdrawals[0]
for w in withdrawals:
    if w > largest_withdrawal:
        largest_withdrawal = w
# Outputs print karte hain [cite: 27]
print("Current Balance:", current_balance)
print("Deposits:", deposits) 
print("Withdrawals:", withdrawals) 
print("Largest Deposit:", largest_deposit) 
print("Largest Withdrawal:", largest_withdrawal) 
