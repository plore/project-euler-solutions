multiple_of_three = range(3, 1000, 3)
multiple_of_five = range(5, 1000, 5)
multiple_of_fifteen = range(15, 1000, 15)

print(sum(multiple_of_three) + sum(multiple_of_five) - sum(multiple_of_fifteen))
