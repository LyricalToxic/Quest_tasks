def is_palindrome(str):
    for x in range(len(str) // 2):
        if str[x] != str[len(str) - x - 1]:
            return False
    return True


a = '123454321'
b = '123456654321'
c = '123453421'
print(is_palindrome(a), is_palindrome(b), is_palindrome(c))
