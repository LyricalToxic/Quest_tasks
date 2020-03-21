import random


def max_number(numbers):
    max_num = numbers[0]
    for x in numbers:
        if x > max_num:
            max_num = x
    return max_num


n = 20
x = [random.randrange(0, n*2) for i in range(n)]
y = [random.randrange(0, n) for i in range(n)]
z = [random.randrange(0, n*3) for i in range(n)]

print(x, max_number(x))
print(y, max_number(y))
print(z, max_number(z))

# print(max(x))
# print(sorted(x)[len(x)-1])
