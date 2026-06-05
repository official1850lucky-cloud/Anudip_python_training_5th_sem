#create a list of 20 numbers and ask the number to remove all its duplicate in list
list=[]
#input 20 numbers in list
for i in range(20):
    num=int(input("Enter a number: "))
    list.append(num)
element=int(input("Enter the number to remove duplicates: "))
#finding the frequency of givenuber
frequency=list.count(element)
if frequency==0:
    print("Element not found in list.")
elif frequency==1:
    print("No duplicates found for the element.")
#reversing the list to remove duplicates from the end
list.reverse()
for i in range(1,frequency):
    list.remove(element)
#again reverse the list to maintain original order
list.reverse()
print("List after removing duplicates:", list)
