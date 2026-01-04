import time
from collections import defaultdict


type Point2D = tuple[int, int]
largest_square: tuple[Point2D, Point2D] | None = None
largest_square_size = 0
start_time = time.perf_counter()

square_map: dict[int, list[int]] = defaultdict(list)

with open('python/day9/data.txt', 'r') as f:
  rows = f.readlines()
  for i, line in enumerate(rows):
    x, y = line.split(',')
    square_map[int(y)].append(int(x))

def square_size(p1: Point2D, p2: Point2D) -> int:
  x1, y1 = p1
  x2, y2 = p2
  return ((abs(x1 - x2) + 1) * abs((y1 - y2) + 1))

for row in square_map.keys():
  for col in square_map[row]:
    root_square = (row, col)
    # Just go through every row and get min and max col to form a square
    for compare_row in square_map.keys():
      min_col, max_col = min(square_map[compare_row]), max(square_map[compare_row])
      # print(square_size(root_square, (compare_row, min_col)), "->", root_square, (compare_row, min_col))
      # print(square_size(root_square, (compare_row, min_col)), "->", root_square, (compare_row, min_col))
      if square_size(root_square, (compare_row, min_col)) > largest_square_size:
        largest_square_size = square_size(root_square, (compare_row, min_col))
        largest_square = (root_square, (compare_row, min_col))
      if square_size(root_square, (compare_row, max_col)) > largest_square_size:
        largest_square_size = square_size(root_square, (compare_row, max_col))
        largest_square = (root_square, (compare_row, max_col))

end_time = time.perf_counter() - start_time
print("Largest square:", largest_square_size, largest_square)
print(f"Time: {(end_time * 1000):.4f} ms")