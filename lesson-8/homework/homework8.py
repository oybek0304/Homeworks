# =============================
# Exception Handling Exercises
# =============================

# 1. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. ValueError
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not a valid integer.")

# 3. FileNotFoundError
try:
    with open("non_existing_file.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")

# 4. ValueError (incorrect input type)
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = float(a) + float(b)
except ValueError:
    print("Input must be numerical.")

# 5. PermissionError (might not raise error on all systems)
try:
    with open("/root/secret_file.txt") as f:
        data = f.read()
except PermissionError:
    print("Permission denied.")

# 6. IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index is out of range.")

# 7. KeyboardInterrupt
try:
    num = input("Press Ctrl+C to cancel: ")
except KeyboardInterrupt:
    print("Input cancelled.")

# 8. ArithmeticError
try:
    result = 1 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

# 9. UnicodeDecodeError (make sure 'file.txt' contains non-ASCII characters)
try:
    with open("file.txt", encoding="ascii") as f:
        data = f.read()
except UnicodeDecodeError:
    print("Unicode decode error.")

# 10. AttributeError
try:
    my_list = [1, 2, 3]
    my_list.push(4)
except AttributeError:
    print("Attribute error occurred.")

# =============================
# File Input/Output Exercises
# =============================

# 1. Read entire file
with open("sample.txt") as f:
    print(f.read())

# 2. Read first n lines
n = 3
with open("sample.txt") as f:
    for i in range(n):
        print(f.readline())

# 3. Append text to file
with open("sample.txt", "a") as f:
    f.write("\nAppended line.")
with open("sample.txt") as f:
    print(f.read())

# 4. Read last n lines
from collections import deque
with open("sample.txt") as f:
    last_lines = deque(f, maxlen=3)
    print(''.join(last_lines))

# 5. Read lines to list
with open("sample.txt") as f:
    lines = f.readlines()
    print(lines)

# 6. Read lines to variable
with open("sample.txt") as f:
    text = f.read()
    print(text)

# 7. Read lines to array (same as list in Python)
with open("sample.txt") as f:
    arr = f.readlines()
    print(arr)

# 8. Find longest word(s)
with open("sample.txt") as f:
    words = f.read().split()
longest = max(words, key=len)
print(longest)

# 9. Count lines
with open("sample.txt") as f:
    print(len(f.readlines()))

# 10. Word frequency (case-insensitive)
from collections import Counter
with open("sample.txt") as f:
    words = f.read().lower().split()
    print(Counter(words))

# 11. File size
import os
print(os.path.getsize("sample.txt"))

# 12. Write list to file
items = ["apple", "banana", "cherry"]
with open("output.txt", "w") as f:
    f.write("\n".join(items))

# 13. Copy file
with open("sample.txt") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

# 14. Combine lines from 2 files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for a, b in zip(f1, f2):
        print(a.strip() + " " + b.strip())

# 15. Read random line
import random
with open("sample.txt") as f:
    lines = f.readlines()
    print(random.choice(lines))

# 16. Check if file is closed
f = open("sample.txt")
f.close()
print(f.closed)

# 17. Remove newline characters
with open("sample.txt") as f:
    lines = [line.strip() for line in f]
    print(lines)

# 18. Word count
with open("sample.txt") as f:
    text = f.read().replace(",", " ")
    print(len(text.split()))

# 19. Extract characters from all .txt files in directory
char_list = []
for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(filename) as f:
            char_list.extend(f.read())
print(f"Total characters collected: {len(char_list)}")

# 20. Generate A-Z files
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")

# 21. Alphabet file with letters per line
line_length = 5
with open("alphabet.txt", "w") as f:
    for i in range(0, 26, line_length):
        f.write("".join(string.ascii_uppercase[i:i+line_length]) + "\n")
