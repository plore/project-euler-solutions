with open("059.txt", "r") as f:
    letters = [int(c) for c in f.read().split(",")]


def decrypt(text: list[int], key: list[int]) -> list[int]:
    n = len(key)
    res = [0] * len(text)
    for i, char in enumerate(text):
        res[i] = char ^ key[i % n]
    return res


for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            cleartext = decrypt(letters, [a, b, c])
            english_text = "".join([chr(c) for c in cleartext])
            if " the " in english_text:
                print(sum(cleartext))
                break
