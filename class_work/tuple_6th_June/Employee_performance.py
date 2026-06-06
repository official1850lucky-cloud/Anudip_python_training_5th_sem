# # Employee records stored in a tuple
# every employee contain:
# First value = Employee ID 
# Second value = Employee Name 
# Third value = Performance Score
# -----------------------------------------------
# 1. Display details of employees scoring 80 or above. 
# 2. Count the number of employees who need improvement (score below 60).  
# 3. Find the employee with the highest score.
# 4. Create a list containing the names of all employees scoring above 75.
# 5. Display the performance category for each employee:  
#   o 90 and above → Excellent 
#   o 75 to 89 → Good 
#   o 60 to 74 → Average 
#   o Below 60 → Needs Improvement  
# --------------------------------------------------------
# creating employee data
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)
# Task 1: Display details of employees scoring 80 or above
print("Employees Scoring 80 or Above:")
for emp_id, name, score in employees:
    if score >= 80:
        print(f"{emp_id} {name} {score}")
print("--------------------------------") 
# Task 2: Count the number of employees who need improvement (score below 60)
improvement_count = 0
for emp in employees:
    if emp[2] < 60:
        improvement_count += 1
print(f"Employees Needing Improvement: {improvement_count}")
print("-------------------------------------") 
# Task 3: Find the employee with the highest score
# Initialize with the first employee's data
highest = employees[0] 
for emp in employees[1:]:
    if emp[2] > highest[2]:
        highest_performer = emp
print(f"Highest Performer: {highest[0]} {highest[1]} {highest[2]}")
print("-------------------------------------------") 
# Task 4: Create a list containing the names of all employees scoring above 75
high = []
for emp_id, name, score in employees:
    if score > 75:
        high.append(name)
print(f"High Performers: {high}")
print("-------------------------------------") 
# Task 5: Display the performance category for each employee
print("Performance Categories:")
for emp_id, name, score in employees:
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print(f"{name} - {category}")