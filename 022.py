with open("22.txt", "r") as f:
    names = f.read().replace('"', "").split(",")

names.sort()

name_values = [sum([ord(c) - ord("A") + 1 for c in name]) for name in names]

name_scores = [(i + 1) * name_value for i, name_value in enumerate(name_values)]

print(sum(name_scores))
