from helpers import is_palindrome

largest = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):  # avoid checking products twice
        if is_palindrome(i * j):
            largest = max(largest, i * j)
            break  # smaller j will only produce smaller palindromes

print(largest)
