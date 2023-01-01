# At 200000, we will have 9 * 1 + 90 * 2 + 900 * 3 + 9000 * 4 + 90000 * 5 + 100000 * 6
# = 1088889 digits

s = "".join([str(n) for n in range(1, 200000)])

print(
    int(s[0])
    * int(s[9])
    * int(s[99])
    * int(s[999])
    * int(s[9999])
    * int(s[99999])
    * int(s[999999])
)
