# Accept marks of 5 subjects
total = 0
failed_subjects = 0
print("marks should be 0 to 100")
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks
    # Count failed subjects
    if marks < 40:
        failed_subjects += 1
# Calculate percentage
percentage = total / 5
# Determine grade
if percentage >= 90 and <75:
    grade = "A+"
elif percentage >= 75 and <60:
    grade = "A"
elif percentage >= 60 and <40:
    grade = "B"
elif percentage >= 40 and <30:
    grade = "C"
else:
    grade = "Fail"
# Display results
print("\n----- Result -----")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Number of Subjects Failed:", failed_subjects)
