import numpy as np

# array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#                   [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#                   [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
# # print(array)
# print(np.sum(array, axis=0))
# print(np.sum(array, axis=1))
# print(np.sum(array, axis=2))

# word = array [1, 2, 0] + array [0, 0, 0] + array [1, 2, 2] + array [2, 0, 1] + array [2, 2, 0]
# print(word)

# array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# print(array)
# print(np.sum(array, axis=1))

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 ** array2)

#Comparison Operators
# scores = np.array([91, 55, 100, 73, 82, 64])

# scores[scores < 60] = "Fail"
# print(scores)

# array1 = np.array([[1, 2, 3, 4]])
# array2= np.array([[1], [2], [3], [4]])
# print(array1.shape)
# print(array2.shape)
# print(array1 * array2)

# array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np.sum(array, axis=0))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.mean(array))
# print(np.argmax(array))
# print(np.argmin(array))

#filtering
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])
# teenagers = ages[ages < 18]
# print(teenagers)
# adults = ages[(ages >= 18) & (ages < 65)]
# print(adults)
# seniors = ages[ages >= 65]
# print(seniors)
# evens = ages[ages%2 == 0]
# print(evens)
# odds = ages[ages%2 == 1]
# print(odds) 

#Using the where function to preserve the original shape of the array
# adults = np.where(ages >= 18, ages, 0)
# print(adults)


#Random numbers
# rng = np.random.default_rng(seed=2)
# print(rng.integers(1, 101, size=(3, 2)))

#Random floats
# print(np.random.uniform(-1, 1, size=(3, 2)))


#Choice method
rng = np.random.default_rng()
fruits = np.array(["apple", "banana", "coconut", "orange", "pineapple"])
fruits = rng.choice(fruits, size = (3, 3))
print(fruits)