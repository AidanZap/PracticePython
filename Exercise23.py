with open('one.txt', 'r') as file:
    one = file.readlines()

with open('two.txt', 'r') as file:
    two = file.readlines()

overlap = []
for num in one:
    if num in two:
        overlap.append(int(num))

print(overlap)