student_name = input("Enter your name: ")
print(f"Welcome {student_name}! Please enter your marks.")

#Marks input
physics = int(input("Enter marks for physics: "))
chemistry = int(input("Enter marks for chemistry: "))
mechanics = int(input("Enter marks for mechanics: "))

#calculating marks
total_marks = physics + chemistry + mechanics
Avg_marks = total_marks/3
print( )


#calculating grades
if 80 <= Avg_marks <= 100:
    grade = "A+"
elif 70 <= Avg_marks < 80:
    grade = "A"
elif 60 <= Avg_marks < 70:
    grade = "B"
elif 50 <= Avg_marks < 60:
    grade = "C"
else:
    grade = "F"

# Printing student profile
print("====Student Profile====")
print(f"Student Name: {student_name}.")
print(f"Total Marks: {total_marks}.")
print(f"Average Marks: {Avg_marks}.")

#printing grades
if grade == "A+":
    print(f"You have got {grade} grade. Excellent! Keep up the great work!")
elif grade == "A":
    print(f"You have got {grade} grade. Very good! You are doing a great job!")
elif grade == "B":
    print(f"You have got {grade} grade. Good! Keep working hard to improve.")
elif grade == "C":
    print(f"You have got {grade} grade. You passed, but you can do better.")
else:
    print(f"You have got {grade} grade. Unfortunately, you failed. Don't give up, try harder!")

print( )
print("****Thank You*****")