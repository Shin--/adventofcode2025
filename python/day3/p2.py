import time


start_time = time.perf_counter()

joltage_sums = 0
with open('python/day3/data.txt', 'r') as f:
  for l in f.readlines():
    joltages = list(l.strip())
    batteries: list[str] = list()
    offset_left = 0
    for offset_right in range(-11, 1):
      bank_slice = joltages[offset_left:(offset_right if offset_right < 0 else None)]
      battery = max(bank_slice)
      batteries.append(battery)
      offset_left += bank_slice.index(battery) + 1
    joltage_sums += int("".join(batteries))

end_time = time.perf_counter() - start_time
print("Joltage sum:", joltage_sums)
print(f"Time: {(end_time * 1000):.4f} ms")