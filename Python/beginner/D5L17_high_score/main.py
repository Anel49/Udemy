# Input a list of student scores
# example input: "78 65 89 86 55 91 64 89"
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
hscore = student_scores[0]
for x in student_scores:
  if x > hscore:
    hscore = x

print(f"The highest score in the class is: {hscore}")
