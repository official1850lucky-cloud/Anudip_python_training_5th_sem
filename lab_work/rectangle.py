# WAP to calculate Area and Perimeter of a Rectangle 
print("------Rectangle--------")
length = float(input("Enter length: "))
if length < 0:
    exit("Length must be positive numbers.")
width = float(input("Enter width: "))
if width < 0:
    exit("width must be positive numbers.")  
else:
    print("Area of Rectangle =", length * width)
    print("Perimeter of Rectangle =", 2 * (length + width))