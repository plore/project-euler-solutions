# break down letter counts to repeating patterns and add them manually

letters_to_nine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4     # "one", "two", "three", ...
letters_ten_to_nineteen = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 # "ten", "eleven", "twelve", ...
letters_tens = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6            # "twenty", "thirty", "forty", ...

letters_to_ninety_nine = 9 * letters_to_nine + 10 * letters_tens + letters_ten_to_nineteen

letters_above_hundred = 100 * letters_to_nine + 9 * (100 * len("hundred") + 99 * len("and") + letters_to_ninety_nine)
letters_total = letters_to_ninety_nine + letters_above_hundred + len("onethousand")

print(letters_total)
