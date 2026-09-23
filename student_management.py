# Student Management System

class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email          
        self.age = age
        self.department = department
        self.__marks = marks or []    
        
    # Getter for private email
    def get_email(self):
        return self.__email

    # Setter for private email
    def set_email(self, email):
        self.__email = email

    # Method Overloading using default argument
    def add_marks(self, *marks):
    
        for mark in marks:
            if 0 <= mark <= 100:
                self.__marks.append(mark)
            else:
                print(f"Invalid mark: {mark}")

    def display_info(self):
        print("\n----- Student Information -----")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Email      : {self.__email}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")

    def calculate_result(self):
        if not self.__marks:
            return "No marks available"

        average = sum(self.__marks) / len(self.__marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"


# Child Class 1
class UndergraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, semester, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.semester = semester

    # Method Overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester   : {self.semester}")


# Child Class 2
class GraduateStudent(Student):

    def __init__(self, name, student_id, email, age, department, research_topic, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic : {self.research_topic}")

# Creating Objects

student1 = Student(
    "Rahim",
    "ST001",
    "rahim@gmail.com",
    20,
    "Computer Science"
)

student2 = UndergraduateStudent(
    "Karim",
    "ST002",
    "karim@gmail.com",
    21,
    "Computer Science",
    "6th Semester"
)

student3 = GraduateStudent(
    "Sakib",
    "ST003",
    "sakib@gmail.com",
    25,
    "Computer Science",
    "Artificial Intelligence in Healthcare"
)

# Adding Marks

student1.add_marks(75, 82, 68)
student2.add_marks(88, 91, 84)
student3.add_marks(92, 89, 95)

# Display Student Information

student1.display_info()
print("Student Type:", student1.get_student_type())
print("Result      :", student1.calculate_result())

student2.display_info()
print("Student Type:", student2.get_student_type())
print("Result      :", student2.calculate_result())

student3.display_info()
print("Student Type:", student3.get_student_type())
print("Result      :", student3.calculate_result())

# Polymorphism

print("\n========== POLYMORPHISM DEMONSTRATION ==========")

students = [student1, student2, student3]

for student in students:
    print(
        f"{student.name} -> "
        f"{student.get_student_type()}"
    )

# Encapsulation Demonstration

print("\n========== ENCAPSULATION DEMONSTRATION ==========")

print("Student Email:", student1.get_email())

student1.set_email("rahim_new@gmail.com")

print("Updated Email:", student1.get_email())