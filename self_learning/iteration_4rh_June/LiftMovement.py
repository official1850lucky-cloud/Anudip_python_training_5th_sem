# Lift starts at floor 0. User enters destination floors. Display floors travelled per trip, total floors travelled, and stop when user enters -1.
current_floor = 0
total_travelled = 0
print("Current Floor:", current_floor)
while True:
    destination = int(input("Enter Destination (-1 to 80): "))
    if destination < -1 or destination > 80:
        exit("Invalid floor. Please enter a floor between -1 and 80.")
    if destination == -1:
        break
    # Use abs() to calculate difference whether lift moves up or down
    trip_travelled = abs(destination - current_floor)
    total_travelled += trip_travelled
    print("Travelled: ", trip_travelled, " floors")
    # Update current position state to the new location floor
    current_floor = destination
print("Total Travelled: ", total_travelled, " floors")