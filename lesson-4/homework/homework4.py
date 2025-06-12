
# Dictionary  exercises
# 1 masala

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

asc_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)

desc_sorted = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)

# 2 masala

d = {0: 10, 1: 20}
d[2] = 30
print(d)

# 3 masala

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)

# 4 masala

n = 5
squares_dict = {x: x*x for x in range(1, n+1)}
print(squares_dict)

# 5 masala

squares = {x: x**2 for x in range(1, 16)}
print(squares)

# Set exercises
# 1 masala

my_set = {1, 2, 3, 4,5,6,7}
print(my_set)

# 2 masala 

my_set = {10, 20, 30,40}
for item in my_set:
    print(item)

# 3 masala

my_set = {1, 2}
my_set.add(3)
my_set.update([4, 5])
print(my_set)

# 4 masala

my_set = {1, 2, 3, 4}
my_set.remove(3) 
print(my_set)

# 5 masala

my_set = {10, 20, 30}
my_set.discard(20)
print(my_set)
