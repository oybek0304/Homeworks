# Homework
Homework:
1. Given a side of square. Find its perimeter and area.
2. Given diameter of circle. Find its length.
3. Given two numbers a and b. Find their mean.
4. Given two numbers a and b. Find their sum, product and square of each number.

# 1 masala
a = int(input("Enter the side of the Square:"))
perimeter = 4 * a
Area = a * a
print(perimeter)
print(Area)

# 2 masala

d = int(input("Enter the diameter of the Circle:"))
Length = 3.14 * d
print(Length)

# 3 masala

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
mean = (a+b) / 2 
print(mean)

# 4 masala

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))         
sum = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2
print(f"Sum: {sum}, Product: {product}, Square of a: {square_a}, Square of b: {square_b}")
