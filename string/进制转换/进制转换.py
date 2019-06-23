from string import digits, ascii_lowercase, ascii_uppercase

Alphabet = digits + ascii_lowercase + ascii_uppercase

print(Alphabet) # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

"""
10进制转任意进制
"""
# 递归法
def ten2any(n, base=62):
    assert base <= 62
    n, index = divmod(n, base)  # n = n // b, index = n % b
    if n > 0:
        return ten2any(n, base) + Alphabet[index]
    else:
        return Alphabet[index]


print(ten2any(10, 16))
print(ten2any(10, 2))


# 迭代法
def ten2any(n, base=62):
    ret = ""
    while n > 0:
        n, index = divmod(n, base)
        ret = Alphabet[index] + ret
    return ret


print(ten2any(10, 16))
print(ten2any(10, 2))


# 堆栈法
def ten2any(n, base=62):
    stack = []
    while n > 0:
        n, index = divmod(n, base)
        stack.append(Alphabet[index])
    ret = ""
    while stack:
        ret += stack.pop()
    return ret


print(ten2any(10, 16))
print(ten2any(10, 2))

"""
任意进制转10进制
"""

def any2ten(s, base=62):
    n = 0
    length = len(s)
    for i, c in enumerate(s):
        index = Alphabet.index(c)
        n += index * pow(base, length - i - 1)
    return n


print(any2ten('1010', 2))
print(any2ten('13', 8))
