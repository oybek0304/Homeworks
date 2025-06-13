
# 1. Modify String with Underscores
def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0
    count = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3 and i < len(txt) - 1:
            if txt[i] not in vowels and (i + 1 >= len(txt) or txt[i+1] != '_'):
                result += "_"
                count = 0
            else:
                count -= 1
        i += 1
    return result

print("1. Modify String with Underscores:")
print(insert_underscores("hello"))
print(insert_underscores("assalom"))
print(insert_underscores("abcabcabcdeabcdefabcdefg"))
print()


# 2. Integer Squares
print("2. Integer Squares:")
n = int(input("Enter n (1-20): "))
for i in range(n):
    print(i * i)
print()


# 3. Loop-Based Exercises

# Exercise 1
print("3.1 First 10 natural numbers:")
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2
print("\n3.2 Number Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Exercise 3
print("\n3.3 Sum from 1 to n:")
n = int(input("Enter number: "))
print("Sum is:", sum(range(1, n+1)))

# Exercise 4
print("\n3.4 Multiplication Table:")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)

# Exercise 5
print("\n3.5 Filtered List Elements:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100:
        if num % 5 == 0:
            print(num)

# Exercise 6
print("\n3.6 Count Digits:")
num = input("Enter a number: ")
print("Total digits:", len(num))

# Exercise 7
print("\n3.7 Reverse Number Pattern:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Exercise 8
print("\n3.8 Reverse List:")
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# Exercise 9
print("\n3.9 Numbers from -10 to -1:")
for i in range(-10, 0):
    print(i)

# Exercise 10
print("\n3.10 Loop with Done:")
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11
print("\n3.11 Prime Numbers 25–50:")
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12
print("\n3.12 Fibonacci up to 10 terms:")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# Exercise 13
print("\n3.13 Factorial:")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")
print()


# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for k in (c1.keys() | c2.keys()):
        diff = abs(c1[k] - c2[k])
        if diff > 0:
            result.extend([k] * diff)
    return result

print("4. Uncommon Elements:")
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))       
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  
