n = int(input("How many numbers do you want to enter? "))
max_len = 0
current_len = 0
previous_num = None
for i in range(n):
    current_num = float(input(f"Enter number {i+1}: "))
    # First number initialization
    if previous_num is None:
        current_len = 1
        max_len = 1
    # Check if the sequence continues to increase
    elif current_num > previous_num:
        current_len += 1
    else:
        # Sequence broke, reset continuous counter to 1
        current_len = 1
    # Update max length tracker if current stretch is longer
    if current_len > max_len:
        max_len = current_len
    # Keep track of this number for the next comparison loop
    previous_num = current_num

print(f"Longest Sequence Length = {max_len}")
