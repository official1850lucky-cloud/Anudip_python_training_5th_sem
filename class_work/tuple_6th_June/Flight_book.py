# Flight booking system
# data contains:
# Passenger ID, Destination, Booking Status
# Task 1: Display all passengers whose booking status is Confirmed
# Task 2: Count the number of passengers travelling to Delhi
# Task 3: Count Confirmed, Waiting, and Cancelled bookings separately
# Task 4: Create a list containing passenger IDs with Waiting status
# Task 5: Determine which destination has the highest number of bookings
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)
# Task 1: Display all passengers whose booking status is Confirmed
print("Confirmed Passengers:")
for p_id, destination, status in bookings:
    if status == "Confirmed":
        print(f"{p_id} {destination}")
print("---------------------------------")
# Task 2: Count the number of passengers travelling to Delhi
delhi_count = 0
for p_id, destination, status in bookings:
    if destination == "Delhi":
        delhi_count += 1
print(f"Passengers Travelling to Delhi: {delhi_count}")
print("--------------------------------------")
# Task 3: Count Confirmed, Waiting, and Cancelled bookings separately
confirmed = 0
waiting = 0
cancelled = 0
for p_id, destination, status in bookings:
    if status == "Confirmed":
        confirmed += 1
    elif status == "Waiting":
        waiting += 1
    elif status == "Cancelled":
        cancelled += 1
print(f"Confirmed: {confirmed}")
print(f"Waiting: {waiting}")
print(f"Cancelled: {cancelled}")
print("--------------------------------------")
# Task 4: Create a list containing passenger IDs with Waiting status
waiting_list = []
for id, destination, status in bookings:
    if status == "Waiting":
        waiting_list.append(p_id)
print(f"Waiting List: {waiting_list}")
print("---------------------------------------")
# Task 5: Determine which destination has the highest number of bookings
delhi = 0
mumbai = 0
chennai = 0
#check for which destonation booked most
for i in bookings:
    if i[1] == "Delhi":
        delhi += 1
    elif i[1] == "Mumbai":
        mumbai += 1
    elif i[1] == "Chennai":
        chennai += 1
if delhi > mumbai and delhi > chennai: #checking for delhi if it is most booked
    most_booked = "Delhi"
elif mumbai > delhi and mumbai > chennai: #checking for mumbai if it is most booked
    most_booked = "Mumbai"
else:
    most_booked = "Chennai" # checking for chennai if it is most booked
print("Most Booked Destination :", most_booked)


