def is_palindrome(x: int) -> bool:
    l = list(str(x))[::-1]
    return int("".join(l)) == x


largest = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):  # avoid checking products twice
        if is_palindrome(i * j):
            largest = max(largest, i * j)
            break  # smaller j will only produce smaller palindromes

print(largest)
