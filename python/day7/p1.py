import time
from typing import TypedDict
import numpy as np

class SplittersRow(TypedDict):
  x: np.ndarray

start_time = time.perf_counter()
splitters_map: dict[int, SplittersRow] = {}
x_positions: set[int] = set()
splitters: list[tuple[int, int]] = []
with open('python/day7/data.txt', 'r') as f:
  rows = f.readlines()
  for i, row in enumerate(rows):
    cols = np.array(list(row.strip()))
    if not len(x_positions):
      start_pos_matches = np.where(cols == 'S')[0]
      if len(start_pos_matches):
        x_positions.add(int(start_pos_matches[0]))
        continue
    splitter_matches = np.where(cols == '^')[0]
    if len(splitter_matches):
      splitters_map[i] = {'x': splitter_matches}


for pos_y in sorted(splitters_map.keys()):
  splitter_positions = splitters_map[pos_y]['x']
  new_x_positions_list = []
  for pos_x in x_positions:
    if pos_x in splitter_positions:
      new_x_positions_list += [pos_x-1, pos_x+1]
      splitters.append((pos_y, pos_x))
    else:
      new_x_positions_list.append(pos_x)
  x_positions = set(new_x_positions_list)


end_time = time.perf_counter() - start_time
print("Splitters hit:", len(set(splitters)))
print(f"Time: {(end_time * 1000):.4f} ms")