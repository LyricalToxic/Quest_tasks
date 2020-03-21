import random


def binary_search(data, value, l=0, r=0):
    if r == 0:
        r = len(data) - l
    len_data_div2 = (l + r) // 2

    if data[len_data_div2] == value:
        return len_data_div2
    elif r - l <= 1:
        print("No matches found.")
        return
    elif data[len_data_div2] < value:
        return binary_search(data, value, len_data_div2, r)
    else:
        return binary_search(data, value, l, len_data_div2)


n = 20
data = (sorted([random.randrange(0, n) for x in range(n)]))
print(data)
if binary_search(data, 15):
    print(binary_search(data, 15))
