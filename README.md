# Python Beginner Projects

This repository contains two simple Python projects created to practice basic Python programming concepts such as functions, input validation, exception handling, and file handling.

---

## 📁 Projects

### Project 1: Greeting Program with Name Validation

#### 📌 Description

This program asks the user to enter their name and displays a welcome message.

It also validates the input to make sure that the name contains only alphabetic characters. If an invalid name is entered, the program displays an error message.

#### 🎯 Objectives

- Take the user's name as input.
- Validate the entered name.
- Create and use a Python function.
- Handle invalid input using `ValueError`.

#### 💻 Code

```python
def greet(name):
    print(f"Hello {name}. Welcome to my program.")

try:
    your_name = input("Enter your name: ")

    if not your_name.isalpha():
        raise ValueError("Invalid name")

    greet(your_name)

except ValueError:
    print("Sorry, you entered an invalid name.")
```

#### ▶️ Example

**Input:**

```text
Enter your name: Arnab
```

**Output:**

```text
Hello Arnab. Welcome to my program.
```

**Invalid Input:**

```text
Enter your name: Arnab123
Sorry, you entered an invalid name.
```

#### 📚 Concepts Used

- `input()`
- Functions
- `try-except`
- `ValueError`
- `.isalpha()`
- f-strings

---

## Project 2: Simple File Writing

#### 📌 Description

This program asks the user to enter their name and saves the name into a text file called `name.txt`.

It demonstrates basic file handling in Python.

#### 🎯 Objectives

- Take the user's name as input.
- Create or open a text file.
- Write the name into the file.
- Automatically close the file.

#### 💻 Code

```python
name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

print("Name has been saved successfully.")
```

#### ▶️ Example

**Input:**

```text
Enter your name: Arnab
```

**Output:**

```text
Name has been saved successfully.
```

After running the program, a file named:

```text
name.txt
```

will be created.

The file will contain:

```text
Arnab
```

#### 📚 Concepts Used

- `input()`
- File handling
- `open()`
- Write mode (`"w"`)
- `with` statement
- `file.write()`

---

## 🛠️ Requirements

- Python 3.x
- Any Python IDE or code editor
- Terminal/Command Prompt

---

## ▶️ How to Run

Clone or download this repository and open the project folder in your terminal.

Run Project 1:

```bash
python project1.py
```

Run Project 2:

```bash
python project2.py
```

---

## 📂 Suggested Project Structure

```text
Python-Beginner-Projects/
│
├── project1.py
├── project2.py
├── name.txt
└── README.md
```

---

## 👨‍💻 Author

**Arnab Bose**

Computer Science & Engineering (CSE) Student

---

## 📄 License

This project is created for educational and learning purposes.
