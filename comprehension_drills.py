numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

divisible_by_3 = [num for num in numbers if num % 3 == 0]
print("Divisible by 3:", divisible_by_3)


words = ["python", "java", "computer", "code", "developer", "data"]

long_words = [word.title() for word in words if len(word) > 4]
print("Long words in title case:", long_words)


celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit temperatures:", fahrenheit)



nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

flattened = [num for sublist in nested_list for num in sublist]
print("Flattened list:", flattened)


# Dict Comprehension Example
squares = {x: x**2 for x in range(1, 6)}
print("Dictionary comprehension:", squares)


# Set Comprehension Example
unique_lengths = {len(word) for word in words}
print("Set comprehension:", unique_lengths)
