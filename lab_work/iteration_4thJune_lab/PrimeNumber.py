# Accept a number from the user
num = int(input("Enter a number: "))

factor_count = 0

print("Factors:", end=" ")

# Find and display all factors
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        factor_count += 1

print()

# Check if the number is prime
if factor_count == 2:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
