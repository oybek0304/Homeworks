import numpy as np

# 1. Convert List to 1D Array
print("Task 1:")
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("Original List:", original_list)
print("One-dimensional NumPy array:", array_1d)

# 2. Create 3x3 Matrix (2 to 10)
print("\nTask 2:")
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3)

# 3. Null Vector (10) & Update Sixth Value
print("\nTask 3:")
null_vector = np.zeros(10)
print(null_vector)
null_vector[6] = 11
print("Update sixth value to 11")
print(null_vector)

# 4. Array from 12 to 38
print("\nTask 4:")
array_12_to_38 = np.arange(12, 38)
print(array_12_to_38)

# 5. Convert Array to Float Type
print("\nTask 5:")
original_array = np.array([1, 2, 3, 4])
float_array = original_array.astype(float)
print("Original array")
print(original_array)
print("Converted to float:")
print(float_array)

# 6. Celsius to Fahrenheit Conversion
print("\nTask 6:")
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9 / 5) + 32
print("Values in Centigrade degrees:")
print(celsius)
print("Values in Fahrenheit degrees:")
print(fahrenheit)

# 7. Append Values to Array
print("\nTask 7:")
original_array = np.array([10, 20, 30])
print("Original array:")
print(original_array)
appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:")
print(appended_array)

# 8. Array Statistical Functions
print("\nTask 8:")
random_array = np.random.rand(10)
print("Array:", random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array))

# 9. Find min and max
print("\nTask 9:")
array_10x10 = np.random.rand(10, 10)
print("Min:", np.min(array_10x10))
print("Max:", np.max(array_10x10))

# 10. Create 3x3x3 array with random values
print("\nTask 10:")
array_3x3x3 = np.random.rand(3, 3, 3)
print(array_3x3x3)
