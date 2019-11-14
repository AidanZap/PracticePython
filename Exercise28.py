def max_of_three(a: int, b: int, c: int):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c


print(str(max_of_three(1, 3, 1)))
