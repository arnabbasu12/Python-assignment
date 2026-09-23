# Student Management System

A simple **Student Management System** developed using **Python Object-Oriented Programming (OOP)** concepts.

This project is designed as an academic assignment to demonstrate important OOP concepts such as **classes, objects, inheritance, polymorphism, method overriding, method overloading, and encapsulation**.

---

## 📌 Project Overview

The Student Management System manages different types of students:

* General Student
* Undergraduate Student
* Graduate Student

The system stores student information, manages marks, calculates results, and identifies the type of student.

The project is implemented using pure Python and does not require any external libraries.

---

## 🎯 Objectives

The main objectives of this project are:

* To understand Python classes and objects.
* To implement inheritance.
* To demonstrate polymorphism.
* To practice method overriding.
* To demonstrate method overloading using `*args`.
* To understand encapsulation using private attributes.
* To perform basic student result calculation.
* To organize a Python project using OOP principles.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Programming Concept:** Object-Oriented Programming (OOP)
* **External Libraries:** None
* **Database:** Not Required

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── student_management.py
├── README.md
└── .gitignore
```

### File Description

| File                    | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `student_management.py` | Main Python program containing all classes and functionality |
| `README.md`             | Project documentation                                        |
| `.gitignore`            | Specifies files that should not be uploaded to GitHub        |

---

## 🏗️ Class Structure

The project uses the following class hierarchy:

```text
                    Student
                       |
             +---------+---------+
             |                   |
             ↓                   ↓
 UndergraduateStudent     GraduateStudent
```

---

## 👨‍🎓 Student Class

The `Student` class is the parent class.

### Attributes

```text
name
student_id
email
age
department
```

Private attributes:

```text
__email
__marks
```

### Methods

```python
display_info()
calculate_result()
get_student_type()
add_marks()
get_email()
set_email()
```

---

## 🎓 UndergraduateStudent Class

`UndergraduateStudent` inherits from the `Student` class.

### Additional Attribute

```text
semester
```

Example:

```text
6th Semester
```

### Overridden Method

```python
get_student_type()
```

It returns:

```text
Undergraduate Student
```

---

## 🎓 GraduateStudent Class

`GraduateStudent` also inherits from the `Student` class.

### Additional Attribute

```text
research_topic
```

Example:

```text
Artificial Intelligence in Healthcare
```

### Overridden Method

```python
get_student_type()
```

It returns:

```text
Graduate Student
```

---

# 🧠 OOP Concepts Demonstrated

## 1. Class and Object

Classes are used as blueprints for creating student objects.

Example:

```python
student1 = Student(
    "Rahim",
    "ST001",
    "rahim@gmail.com",
    20,
    "Computer Science"
)
```

Here, `student1` is an object of the `Student` class.

---

## 2. Attributes

The project uses student-related attributes such as:

```python
name
student_id
email
age
department
semester
research_topic
```

These attributes store information about each student.

---

## 3. Methods

The classes contain methods that perform different operations.

For example:

```python
display_info()
```

displays student information.

```python
calculate_result()
```

calculates the average marks and grade.

```python
get_student_type()
```

identifies the type of student.

---

## 4. Inheritance

`UndergraduateStudent` and `GraduateStudent` inherit from `Student`.

```python
class UndergraduateStudent(Student):
```

```python
class GraduateStudent(Student):
```

This allows the child classes to reuse the properties and methods of the parent class.

---

## 5. Method Overriding

The child classes override the `get_student_type()` method.

Parent class:

```python
def get_student_type(self):
    return "General Student"
```

Undergraduate class:

```python
def get_student_type(self):
    return "Undergraduate Student"
```

Graduate class:

```python
def get_student_type(self):
    return "Graduate Student"
```

---

## 6. Polymorphism

Polymorphism allows the same method to behave differently depending on the object.

Example:

```python
students = [student1, student2, student3]

for student in students:
    print(student.get_student_type())
```

Possible output:

```text
Rahim -> General Student
Karim -> Undergraduate Student
Sakib -> Graduate Student
```

The same method:

```python
get_student_type()
```

produces different results for different objects.

---

## 7. Method Overloading

Python does not support traditional method overloading like some other programming languages.

In this project, `*args` is used to allow the `add_marks()` method to accept different numbers of arguments.

```python
def add_marks(self, *marks):
```

It can accept one mark:

```python
student.add_marks(80)
```

or multiple marks:

```python
student.add_marks(80, 75, 90)
```

---

## 8. Encapsulation

Private attributes are used to demonstrate encapsulation.

```python
self.__email
self.__marks
```

The private email can be accessed using:

```python
student.get_email()
```

and modified using:

```python
student.set_email("newemail@gmail.com")
```

This prevents direct access to the private attributes from outside the class.

---

# 📊 Result Calculation

The system calculates the average marks and assigns a grade.

| Average Marks | Grade |
| ------------: | :---: |
|        80–100 |   A+  |
|         70–79 |   A   |
|         60–69 |   B   |
|         50–59 |   C   |
|         40–49 |   D   |
|      Below 40 |   F   |

For example:

```text
Marks: 88, 91, 84

Average: 87.67
Grade: A+
```

---

# ▶️ How to Run the Project

## Step 1: Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

or:

```bash
py --version
```

---

## Step 2: Clone the Repository

Clone this GitHub repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then enter the project directory:

```bash
cd Student-Management-System
```

---

## Step 3: Run the Program

Run:

```bash
python student_management.py
```

If `python` does not work on Windows, try:

```bash
py student_management.py
```

---

# 💻 Sample Output

```text
----- Student Information -----
Name       : Rahim
Student ID : ST001
Email      : rahim@gmail.com
Age        : 20
Department : Computer Science

Student Type: General Student
Result      : Average: 75.00, Grade: A

----- Student Information -----
Name       : Karim
Student ID : ST002
Email      : karim@gmail.com
Age        : 21
Department : Computer Science
Semester   : 6th Semester

Student Type: Undergraduate Student
Result      : Average: 87.67, Grade: A+

----- Student Information -----
Name       : Sakib
Student ID : ST003
Email      : sakib@gmail.com
Age        : 25
Department : Computer Science
Research Topic : Artificial Intelligence in Healthcare

Student Type: Graduate Student
Result      : Average: 92.00, Grade: A+

========== POLYMORPHISM DEMONSTRATION ==========

Rahim -> General Student
Karim -> Undergraduate Student
Sakib -> Graduate Student

========== ENCAPSULATION DEMONSTRATION ==========

Student Email: rahim@gmail.com
Updated Email: rahim_new@gmail.com
```

---

# 📚 Assignment Requirements Checklist

| Requirement                | Status |
| -------------------------- | :----: |
| Student Class              |    ✅   |
| UndergraduateStudent Class |    ✅   |
| GraduateStudent Class      |    ✅   |
| Attributes                 |    ✅   |
| Methods                    |    ✅   |
| Class & Object             |    ✅   |
| Inheritance                |    ✅   |
| Polymorphism               |    ✅   |
| Method Overriding          |    ✅   |
| Method Overloading         |    ✅   |
| Encapsulation              |    ✅   |
| Student Result Calculation |    ✅   |

---

# 🚀 Possible Future Improvements

The project can be expanded in the future by adding:

* Student registration
* Update student information
* Delete student
* Search student by ID
* Student database
* MySQL integration
* GUI using Tkinter
* Web version using Django
* Admin dashboard
* Login and authentication
* GPA calculation
* Course management

---

# 👨‍💻 Author

**Arnab Bose**

Computer Science & Engineering Student

---

# 📄 License

This project was created for **educational and academic purposes**.
