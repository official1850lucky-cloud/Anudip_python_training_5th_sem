# --- Electricity Bill Calculator ---
# 1. User se input lena
units = float(input("Enter the total units consumed: "))
bill = 0.0
# Slab Rates ke mutabik Bill Calculate karna (Slab Logic)
# Agar units 100 ya usse kam hain
if units <= 100:
    bill = units * 5
#Agar units 100 se zyada hain par 200 tak hain
elif units <= 200:
    # Pehle 100 units ka rate Rs 5 ke hisab se (100 * 5 = 500)
    # Aur bachi hui units ka rate Rs 7 ke hisab se
    bill = (100 * 5) + ((units - 100) * 7)
#Agar units 200 se bhi upar nikal gayi hain
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
# Consumption Category decide karna (Conditional Logic)
# Kam use (0-100 units) -> Low Consumption
if units <= 100:
    category = "Low Consumption"
# Medium use (101-200 units) -> Medium Consumption
elif units <= 200:
    category = "Medium Consumption"
# Zyada use (200 se upar) -> High Consumption
else:
    category = "High Consumption"
# 4. Final Output Screen Par Display Karna
print("       ELECTRICITY BILL RECEIPT      ")
print(f"Units Consumed : {units:.1f} units")
print(f"Category       : {category}")
print(f"Total Bill     : ₹{bill:.2f}")

