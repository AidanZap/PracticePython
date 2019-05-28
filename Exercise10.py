#Exercise 10
    #Given two lists, return a list with the common elements (use list comprehension)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = [num for num in a if num in b]
no_repeat = []
for num in common:
    if num not in no_repeat:
        no_repeat.append(num)

print(no_repeat)