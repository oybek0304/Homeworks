# Homework: map, filter, lambda, and function problems

# map() with lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares using map + lambda:", squares)  # [1, 4, 9, 16, 25]

# filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter + lambda:", even_numbers)  # [2, 4]

# Problem 1: is_prime(n)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("is_prime(4):", is_prime(4))  
print("is_prime(7):", is_prime(7))   

# Problem 2: digit_sum(k)

def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print("digit_sum(24):", digit_sum(24))   
print("digit_sum(502):", digit_sum(502))  

# Problem 3: 2 powers <= N

def powers_of_two(N):
    result = []
    power = 1
    while power * 2 <= N:
        power *= 2
        result.append(power)
    return result

print("powers_of_two(10):", powers_of_two(10)) 
