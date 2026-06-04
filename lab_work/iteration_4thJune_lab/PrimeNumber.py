# check whetger a number is prime or not
num = int(input("Koi bhi number enter karein: "))

if num <= 1:
    print(f"{num} prime number nahi hai.")
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Agar kisi se bhi divide ho gaya, to prime nahi hai
            break            

    # Final result check karna
    if is_prime == True:
        print(f"{num} ek Prime Number hai! ")
    else:
        print(f"{num} Prime Number nahi hai. ")