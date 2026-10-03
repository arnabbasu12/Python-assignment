from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_current_datetime(fmt: str = DATETIME_FORMAT) -> str:
    return datetime.now().strftime(fmt)


def main() -> None:
    print()
    print(f"Current Date and Time: {get_current_datetime()}")


if __name__ == "__main__":
    main()
print()