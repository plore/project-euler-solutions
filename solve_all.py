import os
import subprocess
import time

filenames = [f"{num:0>3}.py" for num in range(100 + 1)]
existing_files = [filename for filename in filenames if os.path.exists(filename)]
print(existing_files)

for filename in existing_files:
    start = time.time()
    result = subprocess.run(["python", filename], capture_output=True, check=True)
    end = time.time()
    print(f"{filename.split('.')[0]}: {int(result.stdout.strip())} \t (calculated in {end - start:.1f} seconds)")


