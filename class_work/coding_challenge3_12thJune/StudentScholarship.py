# write a program to analyze Student Scholarship Evaluation System
# Tasks 
# 1. Display students scoring above 85 marks.  
# 2. Find the topper.  
# 3. Find the student with the lowest marks.  
# 4. Calculate class average marks.  
# 5. Generate grades:  
# o A (90+)  
# o B (75–89)  
# o C (50–74)  
# o F (<50)  
# 6. Create a list of scholarship students (marks ≥ 90). 
# ---------------------------------------------------------------------
# create sample data
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
#display students scoring above 85 marks
for mark in marks:
    if marks[mark]>85:
        print(marks)
#find topper 
topper=0
for top in marks:
    if marks[top]>topper:
        topper=marks[top]
        topperone=top
print(f"{topperone} has highest marks")
#3. Find the student with the lowest marks.
lowest=marks["Anuj"]
for low in marks:
    if marks[low]<lowest:
        lowest=marks[low]
        topperone=low
print(f"{topperone} has lowest marks")
#Calculate class average marks.
sum=0
count=0
for avg in marks:
    sum+=marks[avg]
    count+=1
average=sum/count
print(f"Average marks of the class: {average}")  
# Generate grades:
for grade in marks:
    if 100>=marks[grade]>=90:
        print(f"{grade} has A grade")
    if 89>=marks[grade]>=75:
        print(f"{grade} has B grade")
    if 50<=marks[grade]<=74:
        print(f"{grade} has C grade")
    if marks[grade]<50:
        print(f"{grade} has F grade")
# 6. Create a list of scholarship students (marks ≥ 90).
scholarship=[]
for s in marks:
    if marks[s]>=90:
        scholarship.append(s)
print(f"List of Scholarship students:\n {scholarship}")
