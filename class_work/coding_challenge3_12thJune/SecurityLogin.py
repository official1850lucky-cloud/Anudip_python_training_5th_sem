#  write a program to analyze Cyber Security Login Audit System 
# 2. Identify users with more than 2 failed attempts.  
# 3. Create a dictionary storing the number of failures per user.  
# 4. Create a set of users who logged in successfully.  
# 5. Display users whose accounts should be reviewed. 
# Open the file in read mode
file = open("login_logs.txt", "r")       
# Variables to count successful and failed logins
success_count = 0
failed_count = 0
# Dictionary to store failure count of each user
failure_dict = {}
# Set to store users who logged in successfully
success_users = set()
# Read each line from the file
for line in file:
    # Remove extra spaces/newline and split by comma
    data = line.strip().split(",")
    # Skip invalid lines
    if len(data) != 2:
        continue
    username = data[0].strip()
    status = data[1].strip()
    # Count successful logins
    if status == "Success":
        success_count += 1
        success_users.add(username)
    # Count failed logins and update dictionary
    elif status == "Failed":
        failed_count += 1
        if username in failure_dict:
            failure_dict[username] += 1
        else:
            failure_dict[username] = 1
# Close the file
file.close()
# Display total successful and failed login attempts
print("Successful Login Attempts:", success_count)
print("Failed Login Attempts:", failed_count)
# Display failure count for each user
print("\nFailure Count per User:")
for user in failure_dict:
    print(user, ":", failure_dict[user])
# Display users who logged in successfully
print("\nUsers with Successful Logins:", success_users)
# Find accounts requiring review (more than 2 failed attempts)
review_accounts = []
for user in failure_dict:
    if failure_dict[user] > 2:
        review_accounts.append(user)

# Display accounts to be reviewed
print("\nAccounts Requiring Review:")
if len(review_accounts) == 0:
    print("None")
else:
    for user in review_accounts:
        print(user)
