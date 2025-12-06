import time

start_time = time.perf_counter()
joltage_sums = 0
with open('python/day3/data.txt', 'r') as f:
  for l in f.readlines():
    joltages = list(l.strip())
    highest_joltage_left = max(joltages[:-1])
    highest_joltage_right = max(joltages[joltages.index(highest_joltage_left)+1:])
    joltage_sums += int(highest_joltage_left + highest_joltage_right)

end_time = time.perf_counter() - start_time
print("Joltage sum:", joltage_sums)
print(f"Time: {(end_time * 1000):.4f} ms")