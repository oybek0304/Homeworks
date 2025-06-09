# 1. masala

name = input("Enter your name: ")           
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - year_of_birth  
print(f"{name}, you are {age} years old.")

# 2. masala

txt = 'LMaasleitbtui'

car_names = []
current = ''

for char in txt:
    if char.isupper():
        if current:
            car_names.append(current)
        current = char
    else:
        current += char

if current:
    car_names.append(current)

print(car_names)


# 3. masala

txt = 'MsaatmiazD'
car_names = []
current = ''

for char in txt:
    if char.isupper():
        if current:
            car_names.append(current)
        current = char
    else:
        current += char

if current:
    car_names.append(current)

print(car_names)

# 4 masala

txt = "I'am John. I am from London"

start = txt.find("from") + len("from ")
residence = txt[start:]
print(residence)

# 5 masala

user_input = input("Enter a string:")
reversed_string = user_input[::-1]  
print(reversed_string)

# 6 masala 

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Number of vowels:", count)

# 7 masala 

numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(float, numbers.split()))
max_value = max(num_list)
print("Maximum value:", max_value)

# 8 masala

word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# 9 masala

email = input("Enter an email address: ")
domain = email.split('@')[-1]
print("Email domain:", domain)

# 10 masala

import random
import string

length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
