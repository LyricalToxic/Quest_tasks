import random


def bubble_sort(data):
    len_data = len(data)
    for i in range(1, len_data):
        for j in range(1, len_data):
            if data[j - 1] < data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]

    return data


n = 20
data = [random.randint(0, n) for x in range(n)]
print(data)
print(bubble_sort(data))
