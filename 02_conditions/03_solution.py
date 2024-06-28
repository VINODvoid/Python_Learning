# Write A  Program that takes a test score as input and returns the grade of the student.

score = int(input("Enter your test score: \n"))


if score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade ="F"

print(f"Your grade is {grade}")
exit()
print("Did exit work")