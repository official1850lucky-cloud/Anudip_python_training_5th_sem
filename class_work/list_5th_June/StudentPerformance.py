#program to student performance analyzer based on marks
marks = [78,45,92,35,88,40,99,56]
count=0
#display all passed students
for i in marks:
    if i <= 40:
        marks.remove(i)
     #count failed students
        count+=1               
print("Passed students:", marks)
print("Failed Count:", count)
Highest=marks[0]
#find highest marks
for i in marks:
    if i > Highest:
        Highest = i
print("Highest Marks:", Highest)
lowest=marks[0]
#find lowest marks
for i in marks:
    if i < lowest:
       lowest = i
print("Lowest Marks:", lowest)
#creating new list for merit students
merit = []
#finding merit students for marks obtained above 75
for i in marks:
    if i > 75:
        merit.append(i)
print("Merit Students:", merit)