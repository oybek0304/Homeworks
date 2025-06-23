# ===== math_operations.py =====

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    raise ValueError("Cannot divide by zero")


# ===== string_utils.py =====

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# ===== geometry/circle.py =====

import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


# ===== file_operations/file_reader.py =====

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


# ===== file_operations/file_writer.py =====

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


# ===== Example Usage =====

if __name__ == "__main__":
    # Math Operations
    print("Add:", add(5, 3))
    print("Divide:", divide(10, 2))

    # String Utils
    print("Reversed:", reverse_string("hello"))
    print("Vowel Count:", count_vowels("education"))

    # Geometry
    print("Circle Area (r=3):", calculate_area(3))
    print("Circle Circumference (r=3):", calculate_circumference(3))

    # File Operations (demo)
    demo_file = "demo.txt"
    write_file(demo_file, "This is a demo file.")
    print("Read File:", read_file(demo_file))
