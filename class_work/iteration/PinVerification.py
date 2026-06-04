pin = int(input("Enter the PIN:")) 
while pin != 1234:
    print("Incorrect PIN. Tryagain.")
    pin = int(input())  
print("Access Granted")