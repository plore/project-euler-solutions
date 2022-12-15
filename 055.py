from helpers import is_palindrome

lychrel_count = 0
for n in range(1, 10000):
    k = 0
    x = n
    while k < 50:
        x += int(str(x)[::-1])
        k += 1
        if is_palindrome(x):
            break
    if k == 50:
        lychrel_count += 1

print(lychrel_count)
