import argparse
import os
import subprocess
import time

expected_solutions = [
    233168,
    4613732,
    6857,
    906609,
    232792560,
    25164150,
    104743,
    23514624000,
    31875000,
    142913828922,
    70600674,
    76576500,
    5537376230,
    837799,
    137846528820,
    1366,
    21124,
    1074,
    171,
    648,
    31626,
    871198282,
    4179871,
    2783915460,
    4782,
    983,
    -59231,
    669171001,
    9183,
    443839,
    73682,
    45228,
    100,
    40730,
    55,
    872187,
    748317,
    932718654,
    840,
    210,
    7652413,
    162,
    16695334890,
    5482660,
    1533776805,
    5777,
    134043,
    9110846700,
    296962999629,
    997651,
    121313,
    142857,
    4075,
    376,
    249,
    972,
    153,
    26241,
    129448,
    26033,
    28684,
    127035954683,
    49,
    1322,
    272,
    661,
    7273,
    6531031914842725,
    510510,
    8319823,
    428570,
    303963552391,
    7295372,
    402,
    161667,
    190569291,
    71,
    55374,
    73162890,
    40886,
    427337,
    260324,
    425185,
    101524,
    2772,
    1818,
    1097343,
    7587457,
    743,
    1217,
]


filenames = [f"{num:0>3}.py" for num in range(100 + 1)]
existing_files = [filename for filename in filenames if os.path.exists(filename)]
existing_numbers = [int(filename.split(".")[0]) for filename in existing_files]

parser = argparse.ArgumentParser(
    description="Tests and prints solutions for one or more problems."
)
parser.add_argument(
    "problems",
    metavar="N",
    type=int,
    nargs="*",
    help="Numbers of problems to test. Accepts leading zeros (example: 042 037)."
    + "Without given problem numbers will test all solutions.",
)

args = parser.parse_args()

if len(args.problems) > 0:
    test_problem_numbers = [num for num in args.problems if num in existing_numbers]
else:
    test_problem_numbers = existing_numbers


for problem_number in test_problem_numbers:
    filename = f"{problem_number:0>3}.py"

    start = time.time()
    result = subprocess.run(["python", filename], capture_output=True, check=True)
    end = time.time()

    solution = int(result.stdout.strip())
    expected_solution = expected_solutions[problem_number - 1]
    assert (
        solution == expected_solution
    ), f"Problem {problem_number}: expected {expected_solution} but got {solution}"

    print(f"{problem_number}: {solution} \t (calculated in {end - start:.1f} seconds)")
