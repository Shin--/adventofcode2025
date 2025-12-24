from functools import lru_cache
import time
from typing import TypedDict
import numpy as np

class SplittersRow(TypedDict):
  x: np.ndarray

start_time = time.perf_counter()
splitters_map: dict[int, SplittersRow] = {}
start_position: int | None = 0
timelines = 0

with open('python/day7/data.txt', 'r') as f:
  rows = f.readlines()
  for i, row in enumerate(rows):
    cols = np.array(list(row.strip()))
    if not start_position:
      start_pos_matches = np.where(cols == 'S')[0]
      if len(start_pos_matches):
        start_position = int(start_pos_matches[0])
        continue
    splitter_matches = np.where(cols == '^')[0]
    if len(splitter_matches):
      splitters_map[i] = {'x': splitter_matches}

def count_timelines(x_pos: int, y_coords: list[int]):

  @lru_cache(None)
  def follow_timeline(_x_pos: int, y_coords_index: int):
    if y_coords_index >= len(y_coords):
      return 1
    
    y_pos = y_coords[y_coords_index]
    splitter_positions = splitters_map[y_pos]['x']
    if _x_pos in splitter_positions:
      return follow_timeline(_x_pos-1, y_coords_index+1) + follow_timeline(_x_pos+1, y_coords_index+1)
    else:
      return follow_timeline(_x_pos, y_coords_index+1)
    
  return follow_timeline(x_pos, 0)
      

if start_position:
  timelines = count_timelines(start_position, sorted(splitters_map.keys()))
else:
  print("Could not find start position")


end_time = time.perf_counter() - start_time
print("Timelines traversed:", timelines)
print(f"Time: {(end_time * 1000):.4f} ms")