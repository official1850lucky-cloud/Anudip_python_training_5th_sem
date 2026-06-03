# WAP to calculate Simple Interest
print("------Simple Interest--------")
p = float(input("Enter Principal Amount: "))
if p<0:
    exit("Invalid principal input, Values must be positive.")
t = int(input("Enter Time (in years): "))
if t<0:
    exit("Invalid time input, Values must be positive.")
r = float(input("Enter Rate of Interest: "))
if r<0:
    exit("Invalid rate input, Values must be positive.")
else:  
    print("Simple Interest =",(p * r * t) / 100)
    
