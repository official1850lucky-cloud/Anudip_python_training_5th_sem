print("------Triangle--------")
a = float(input("Enter first side: "))
if a <= 0:
    exit("Invalid input. Side length must be positive.")
   
b = float(input("Enter second side: "))
if b <= 0:
    exit("Invalid input. Side length must be positive.")        
c = float(input("Enter third side: "))
if c <= 0:
    exit("Invalid input. Side length must be positive.")    
#find parameter
perimeter = a + b + c
#find semi parameter for area
s = perimeter / 2
#display area and parameter
print("first side ",a ," second side ",b ,"third side ",c )
print("Perimeter of triangle =", perimeter)
print("Area of triangle =",(s * (s - a) * (s - b) * (s - c))**0.5)
