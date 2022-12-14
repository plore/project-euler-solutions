# Skip 1000^1000 as it will have zeros at the end
total = sum(x**x for x in range(1, 1000))

print(str(total)[-10:])
