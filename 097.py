# All operations (multiplication, exponentiation, addition) only make the final number
# bigger. In each step we can therefore focus on the last ten digits.
end_digits = 1
for i in range(7830457):
    end_digits = (end_digits * 2) % 10000000000

end_digits = (end_digits * 28433) % 10000000000 + 1
print(end_digits)
