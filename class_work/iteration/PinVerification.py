pin = int(input("Enter the PIN:"))
if(pin.len()!=4):
    exit("PIN must be 4 digits long.")
while pin != 1234:
    print("Incorrect PIN. Tryagain.")
    pin = int(input())  
print("Access Granted")