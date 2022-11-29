# number the days of week from 0 to 6, starting on Monday

# start with 1900-01-01 (Monday)
day = 0

# advance to 1901-01-01 (1900 was not a leap year)
day = (day + 365) % 7

counter = 1 if day == 6 else 0
for year in range(1901, 2001):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        february = 29
    else:
        february = 28

    month_lengths = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # advance to start of next month
    for m in month_lengths:
        day = (day + m) % 7
        if day == 6:
            counter += 1

print(counter)
