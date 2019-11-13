file_path = 'Training_01.txt'
count = {}


def add_count(category: str):
    if category in count:
        count[category] += 1
    else:
        count[category] = 1


with open(file_path, 'r') as file:
    text = file.readlines()
    for line in text:
        category = line.split('/')[2]
        add_count(category)


for thing in count:
    print(f"{count[thing]} {thing}")
