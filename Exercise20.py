import random

numbers = sorted([random.randint(0, 35) for _ in range(15)])
check_number = 15

def easy_way(numbers, check_number):
    return check_number in numbers


def binary_search(numbers, check_number):
    index = int(len(numbers)/2)
    current_num = numbers[index]
    if check_number == current_num:
        return True
    elif len(numbers) == 1:
        return False
    elif check_number > current_num:
        return binary_search(numbers[index:], check_number)
    else:
        return binary_search(numbers[:index], check_number)


print(f"Easy way: {numbers} | {easy_way(numbers, check_number)}")
print(f"Binary Search: {numbers} | {binary_search(numbers, check_number)}")
