from datetime import date

def days_between_dates(begin: str, end: str) -> int:
    """Return absolute day difference between two ISO dates.

    Example:
        >>> days_between_dates("2024-12-31", "2025-01-03")
        3
    """
    d1 = date.fromisoformat(begin)
    d2 = date.fromisoformat(end)
    return abs((d2 - d1).days)


if __name__ == "__main__":
    print(days_between_dates("2024-12-31", "2025-01-03"))
