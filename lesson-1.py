a = [3, 4, 2, 1, 0, 8, 9, -1, 100, 0]
min = a. pop()
while a:
    b = a.pop()
    if b < min:
        min=b
print(min)