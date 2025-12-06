import re

current_position = 50
at_point_zero = 0
with open('python/day1/data.txt', 'r') as f:
  for l in f.readlines():
    direction, count = re.split(r'(\d+)', l)[:2]
    count = int(count)
    initial_position = current_position
    if direction == 'L':
      current_position -= count
    elif direction == 'R':
      current_position += count
    if current_position == 0:
      at_point_zero += 1
    elif current_position < 0:
      at_point_zero += int(abs(current_position / 100)) + (1 if initial_position != 0 else 0)
      current_position %= 100
    elif current_position > 99:
      at_point_zero += int(abs(current_position / 100))
      current_position %= 100

    # print(direction, count, "->", current_position, "-", at_point_zero)


print(f"Final position: {current_position}")
print(f"Times at 0: {at_point_zero}")