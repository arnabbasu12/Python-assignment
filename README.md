# 🐍 Python Beginner Projects

This repository contains two beginner-friendly Python projects created to practice basic Python programming concepts such as input, variables, arithmetic operations, conditional statements, and f-strings.

---

# 📚 Code 1: Student Grade Calculator

## 📌 Description

The **Student Grade Calculator** is a simple Python program that takes a student's name and marks in three subjects, calculates the total and average marks, determines the student's grade, and displays a personalized message based on the grade.

## ✨ Features

- Takes student's name as input
- Takes marks for:
  - Physics
  - Chemistry
  - Mechanics
- Calculates total marks
- Calculates average marks
- Determines the student's grade
- Displays a different message for each grade
- Uses Python f-strings for formatted output

## 📊 Grading System

| Average Marks | Grade |
|---|---|
| 80–100 | A+ |
| 70–79.99 | A |
| 60–69.99 | B |
| 50–59.99 | C |
| Below 50 | F |

## 🧮 Formula

```text
Total Marks = Physics + Chemistry + Mechanics

Average Marks = Total Marks / 3
```

## ▶️ Example

### Input

```text
Enter your name: Arnab
Welcome Arnab! Please enter your marks.

Enter marks for physics: 85
Enter marks for chemistry: 75
Enter marks for mechanics: 90
```

### Output

```text
==== Student Profile ====
Student Name: Arnab.
Total Marks: 250.
Average Marks: 83.33.
You have got A+ grade. Excellent! Keep up the great work!

**Thank You**
```

---

# 🛒 Code 2: Shopping Discount Calculator

## 📌 Description

The **Shopping Discount Calculator** is a Python program that takes the customer's name and the names and prices of three products. It calculates the subtotal, determines the appropriate discount, calculates the discount amount, and displays the final total.

## ✨ Features

- Takes customer's name as input
- Takes names of three products
- Takes prices of three products
- Calculates subtotal
- Determines discount based on subtotal
- Calculates discount amount
- Calculates final total
- Displays a formatted shopping summary using f-strings

## 💰 Discount System

| Subtotal | Discount |
|---:|---:|
| 5000 or above | 20% |
| 3000–4999 | 10% |
| 1000–2999 | 5% |
| Below 1000 | No discount |

## 🧮 Formula

```text
Subtotal = Price 1 + Price 2 + Price 3

Discount = Subtotal × Discount Rate

Final Total = Subtotal - Discount
```

## ▶️ Example

### Input

```text
Enter customer's name: Rahim
Enter name of product 1: Keyboard
Enter price of product 1: 1500
Enter name of product 2: Mouse
Enter price of product 2: 800
Enter name of product 3: Headphone
Enter price of product 3: 2000
```

### Calculation

```text
Subtotal = 1500 + 800 + 2000
         = 4300

Discount Rate = 10%

Discount = 4300 × 0.10
         = 430

Final Total = 4300 - 430
            = 3870
```

### Output

```text
===== SHOPPING SUMMARY =====

Customer Name: Rahim
Product 1: Keyboard
Price: 1500
Product 2: Mouse
Price: 800
Product 3: Headphone
Price: 2000
Subtotal: 4300
Discount: 430
Final Total: 3870
```

---

# 🛠️ Technologies Used

- Python 3
- `input()`
- Variables
- Arithmetic operators
- `if`, `elif`, `else`
- Comparison operators
- f-strings
- Basic mathematical calculations

No external Python libraries are required.

---

# 📁 Project Structure

```text
Python-Beginner-Projects/
│
├── Code_1/
│   └── student_grade_calculator.py
│
├── Code_2/
│   └── shopping_discount_calculator.py
│
└── README.md
```

---

# ▶️ How to Run

Make sure Python 3 is installed.

Check the Python version:

```bash
python --version
```

Run Code 1:

```bash
python student_grade_calculator.py
```

Run Code 2:

```bash
python shopping_discount_calculator.py
```

---

# 🎯 Learning Objectives

These two projects are designed to help beginners understand:

1. Taking user input
2. Storing data in variables
3. Converting input using `int()` and `float()`
4. Performing arithmetic calculations
5. Using conditional statements
6. Comparing values using operators
7. Applying real-world logic with Python
8. Formatting output using f-strings
9. Creating simple console-based applications

---

# 🚀 Future Improvements

## Student Grade Calculator

- Add more subjects
- Add student ID
- Calculate GPA/CGPA
- Add input validation
- Store multiple students
- Save results to a file
- Create a GUI version

## Shopping Discount Calculator

- Add more products
- Add quantity for each product
- Add tax/VAT calculation
- Add multiple customers
- Add invoice generation
- Add payment options
- Create a GUI version

---

# 👨‍💻 Author

**Arnab Bose**

## 📄 License

These projects are created for **educational and learning purposes**.
