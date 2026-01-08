from operator import itemgetter
import time
from collections import defaultdict


type Point2D = tuple[int, int]
largest_square: tuple[Point2D, Point2D] | None = None
largest_square_size = 0
start_time = time.perf_counter()

square_map: dict[int, list[int]] = defaultdict(list)
squares: list[Point2D] = list()

with open('python/day9/data.txt', 'r') as f:
  rows = f.readlines()
  for i, line in enumerate(rows):
    y, x = line.split(',')
    square_map[int(y)].append(int(x))
    squares.append((int(x), int(y)))

min_x = min(squares, key=itemgetter(0))
max_x = max(squares, key=itemgetter(0))
min_y = min(squares, key=itemgetter(1))
max_y = max(squares, key=itemgetter(1))

def square_size(p1: Point2D, p2: Point2D) -> int:
  x1, y1 = p1
  x2, y2 = p2
  return ((abs(x1 - x2) + 1) * abs(y1 - y2))

def cross_product(o: Point2D, a: Point2D, b: Point2D):
    ax, ay = a
    bx, by = b
    ox, oy = o
    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)

def compute_convex_hull(points: list[Point2D]):
    points = sorted(set(points))

    # Build lower hull
    lower: list[Point2D] = []
    for p in points:
        # While the last 3 points make a right turn (or are straight), pop the middle one
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper: list[Point2D] = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def is_point_inside(point: Point2D, hull_points: list[Point2D]) -> bool:
    """
    Input: point (x, y), list of hull vertices.
    Output: True if inside, False if outside.
    Logic: Draw a horizontal ray to the right. Count intersections. 
           Odd intersections = Inside. Even = Outside.
    """
    x, y = point
    hull_points_total = len(hull_points)
    inside = False

    hull_p1x, hull_p1y = hull_points[0]
    for i in range(hull_points_total + 1):
        hull_p2x, hull_p2y = hull_points[i % hull_points_total]
        
        # Check if ray intersects the edge segment
        # 1. p1y and p2y must be on different sides of y (one above, one below)
        # 2. The intersection x-coord must be to the right of our point
        if y > min(hull_p1y, hull_p2y):
            if y <= max(hull_p1y, hull_p2y):
                if x <= max(hull_p1x, hull_p2x):
                    x_intersections: float | None = None
                    if hull_p1y != hull_p2y:
                        x_intersections = (y - hull_p1y) * (hull_p2x - hull_p1x) / (hull_p2y - hull_p1y) + hull_p1x
                    if hull_p1x == hull_p2x or (x_intersections and x <= x_intersections):
                        inside = not inside
        hull_p1x, hull_p1y = hull_p2x, hull_p2y

    return inside

def find_square_corners(square: Point2D, y: int, x_vals: list[int], hull: list[Point2D]):
  sx, sy = square
  valid_squares: list[Point2D] = list()
  for x in x_vals:
    corner1 = (x, sy)
    corner2 = (sx, y)
    if is_point_inside(corner1, hull) and is_point_inside(corner2, hull):
      valid_squares.append((x, y))
  return valid_squares
   

hull = compute_convex_hull(squares)


for row in square_map.keys():
  for col in square_map[row]:
    root_square = (row, col)
    # Just go through every row and find all squares with all corners inside our hull
    for compare_row in square_map.keys():
      compare_cols = square_map[compare_row]
      valid_squares = find_square_corners(root_square, compare_row, compare_cols, hull)
      for valid_square in valid_squares:
        if square_size(root_square, valid_square) > largest_square_size:
          largest_square_size = square_size(root_square, valid_square)
          largest_square = (root_square, valid_square)


from pprint import pprint
pprint(hull)

# for i in range(9):
#    print("".join(['#' if (i, j) in squares else '.' for j in range(16)]))

# print("=======================")

# hull = compute_convex_hull(squares)
# for i in range(9):
#    print("".join(['#' if (i, j) in hull else '.' for j in range(16)]))
      

end_time = time.perf_counter() - start_time
print("Largest square:", largest_square_size, largest_square)
print(f"Time: {(end_time * 1000):.4f} ms")