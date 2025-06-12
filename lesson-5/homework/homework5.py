# 1. Leap Year Checker
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if it's a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example usage
print("Leap Year Check:")
for y in [2000, 1900, 2024]:
    print(f"{y}: {is_leap(y)}")
print()


# 2. Conditional Statements Based on n
def check_weird(n):
    """
    Classifies the number n according to the given rules.

    Args:
        n (int): A positive integer.

    Returns:
        str: 'Weird' or 'Not Weird' depending on conditions.
    """
    if n % 2 == 1:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


# Input for problem 2
n = int(input("Enter a number (1–100): "))
print(check_weird(n))
print()


# 3. Even Numbers Between Two Numbers
# Solution 1: With if-else
def even_numbers_with_if_else(a, b):
    """
    Finds even numbers between a and b (inclusive) using if-else logic.

    Args:
        a (int): Start number.
        b (int): End number.

    Returns:
        list: List of even numbers in the range.
    """
    if a % 2 == 0:
        return list(range(a, b + 1, 2))
    else:
        return list(range(a + 1, b + 1, 2))


# Solution 2: Without using if-else or any conditional
def even_numbers_no_if_else(a, b):
    """
    Finds even numbers between a and b (inclusive) without using any if-else.

    Args:
        a (int): Start number.
        b (int): End number.

    Returns:
        list: List of even numbers in the range.
    """
    return list(filter(lambda x: x % 2 == 0, range(a, b + 1)))


# Inputs for problem 3
a = int(input("Enter starting number (a): "))
b = int(input("Enter ending number (b): "))

print("Even numbers (with if-else):", even_numbers_with_if_else(a, b))
print("Even numbers (no if-else):", even_numbers_no_if_else(a, b))
