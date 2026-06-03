import numpy as np

# ==========================
# 1. Create an Array
# ==========================
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)

# ==========================
# 2. Masking
# ==========================
mask = arr > 30

print("\nBoolean Mask:")
print(mask)

filtered = arr[mask]

print("\nFiltered Values (greater than 30):")
print(filtered)

# ==========================
# 3. Broadcasting
# ==========================
scaled_arr = arr + 5

print("\nArray after Broadcasting (+5):")
print(scaled_arr)

# ==========================
# 4. Cosine Similarity Function
# ==========================
def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    similarity = dot_product / (norm_v1 * norm_v2)
    return similarity


vec1 = np.array([1, 2, 3])
vec2 = np.array([2, 4, 6])


vec3 = np.array([1, 0, 1])
vec4 = np.array([0, 1, 0])

print("\nCosine Similarity Tests:")

print("Similarity between vec1 and vec2:")
print(cosine_similarity(vec1, vec2))

print("\nSimilarity between vec3 and vec4:")
print(cosine_similarity(vec3, vec4))
