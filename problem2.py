import json
from typing import Any


def create_student(name: str, age: int, department: str) -> dict[str, Any]:
    return {"name": name, "age": age, "department": department}


def to_json(data: dict[str, Any]) -> str:
    return json.dumps(data)


def main() -> None:
    print()
    student = create_student(name="Rahim", age=20, department="CSE")

    try:
        print(to_json(student))
    except TypeError as error:
        print(f"Could not convert to JSON: {error}")

if __name__ == "__main__":
    main()
print()