import numpy as np


arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.arange(1, 11)

arr3 = np.zeros(5)

arr4 = np.linspace(0, 100, 6)


print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nArray 3:")
print(arr3)

print("\nArray 4:")
print(arr4)

print("\n=== Array Information ===")

print("arr1 shape:", arr1.shape)
print("arr1 dtype:", arr1.dtype)
print("arr1 ndim:", arr1.ndim)

print("\narr4 shape:", arr4.shape)
print("arr4 dtype:", arr4.dtype)
print("arr4 ndim:", arr4.ndim)


print("\n=== Indexing ===")

print("First element of arr1:", arr1[0])

print("Last element using negative index:", arr1[-1])


print("\n=== Slicing ===")

print("Elements from index 1 to 3:")
print(arr1[1:4])

print("Subarray from arr2:")
print(arr2[3:8])
