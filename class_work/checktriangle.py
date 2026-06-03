#program to check three angles form a triangle or not
print("------Check Triangle--------")
angle1 = float(input("Enter first angle: "))
if angle1 < 0:
    exit(" angle must be positive.")
#----------------------------------------------------------
angle2 = float(input("Enter second angle: "))
if angle2 < 0:
    exit(" angle must be positive.")
#----------------------------------------------------------
angle3 = float(input("Enter third angle: "))
if angle3 < 0:  
    exit(" angle must be positive.")
#----------------------------------------------------------
#verify trianle formation or not
if angle1 + angle2 + angle3 == 180:
    print("The three angles form a triangle.")
else:
    print("The three angles do not form a triangle.")
