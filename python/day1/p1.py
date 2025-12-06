import re

start_position = 50
at_point_zero = 0
with open('python/day1/data.txt', 'r') as f:
  for l in f.readlines():
    direction, count = re.split(r'(\d+)', l)[:2]
    count = int(count)
    if direction == 'L':
      start_position -= count
    elif direction == 'R':
      start_position += count
    if start_position < 0 or start_position > 99:
      start_position %= 100
    if start_position == 0:
      at_point_zero += 1


print(f"Final position: {start_position}")
print(f"Times at 0: {at_point_zero}")