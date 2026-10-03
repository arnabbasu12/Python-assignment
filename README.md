# Python Basics: datetime and JSON

Two small Python programs demonstrating the standard library's `datetime` and `json` modules.

## Contents

| File | Description |
|------|-------------|
| `problem1.py` | Displays the current date and time |
| `problem2.py` | Converts a student dictionary into a JSON string |

## Requirements

- Python 3.9 or newer
- No third-party packages (standard library only)

## Usage

Run each program from the repository folder:

```bash
python problem1.py
python problem2.py
```

On some systems, use `python3` instead of `python`.

---

## Problem 1: Current Date and Time

Uses the `datetime` module to get the current local date and time and prints it in `YYYY-MM-DD HH:MM:SS` format.

**Example output** (the actual value depends on when you run it):

```
Current Date and Time: 2026-10-03 11:30:45
```

**Key points**

- `datetime.now()` returns the current local date and time.
- `strftime("%Y-%m-%d %H:%M:%S")` formats it as text.

---

## Problem 2: Dictionary to JSON

Creates a dictionary holding a student's name, age, and department, then converts it to a JSON string with the `json` module.

**Input**

```python
student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}
```

**Output**

```
{"name": "Rahim", "age": 20, "department": "CSE"}
```

**Key points**

- `json.dumps()` serializes a Python dictionary into a JSON string.
- Errors from non-serializable values are caught and reported.

---

## Code Structure

Both programs follow the same layout:

- Docstrings and type hints on all functions
- Small, reusable functions
- A `main()` entry point guarded by `if __name__ == "__main__":`

## License

Free to use for learning purposes.
