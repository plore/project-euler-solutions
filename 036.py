from helpers import is_palindrome

total = 0
for n in range(1, 1000000):
    if is_palindrome(n):
        b = int(bin(n)[2:])
        if is_palindrome(b):
            total += n

print(total)
