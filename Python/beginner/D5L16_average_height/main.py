# Input a Python list of student heights
# example input: "180 124 165 173 189 169 146"
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
totalheight = 0

for x in student_heights:
  totalheight = totalheight + x
  
numofstudents = len(student_heights)
avgheight = round(totalheight / numofstudents)

print(f"total height = {totalheight}")
print(f"number of students = {numofstudents}")
print(f"average height = {avgheight}")
