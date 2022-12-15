from helpers import is_prime

n_prime = 0
diagonal_number = 1
step = 2
while True:
    for k in range(3):
        diagonal_number += step
        if is_prime(diagonal_number):
            n_prime += 1
    diagonal_number += step  # on odd square diagonal

    # After finishing the layer with stepsize of step, each diagonal excluding the
    # central 1 has step / 2 numbers for a total of 2 * step + 1 numbers
    if n_prime / (2 * step + 1) < 0.1:
        break
    step += 2

print(step + 1)
