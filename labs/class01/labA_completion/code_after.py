# Write a function that:
# - receives two dates in format YYYY-MM-DD
# - computes the difference in days between them
# - returns the absolute result as an integer
# Include type hints and a docstring with an example.

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

# Example usage:
if __name__ == "__main__":
    print(days_between_dates("2024-12-31", "2025-01-03"))  # Output: 3