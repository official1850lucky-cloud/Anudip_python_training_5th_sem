# Accept number of rows
rows = int(input("Enter number of rows: "))
# Print pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()