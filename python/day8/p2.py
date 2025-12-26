from functools import lru_cache
from math import prod, sqrt
import time


type Point3D = tuple[int, int, int]
type Circuit = set[Point3D]
junction_boxes: list[Point3D] = []
start_time = time.perf_counter()

circuits: list[Circuit] = []
circuit_pointers: dict[Point3D, Circuit] = {}

with open('python/day8/data.txt', 'r') as f:
  rows = f.readlines()
  for i, row in enumerate(rows):
    xyz = row.strip().split(',')
    if len(xyz) != 3:
      raise ValueError
    x, y, z = [int(val) for val in xyz]
    junction_boxes.append((x, y, z))

@lru_cache(4000)
def point_distance(p1: Point3D, p2: Point3D):
  x1, y1, z1 = p1
  x2, y2, z2, = p2
  return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

distance_map: dict[float, tuple[Point3D, Point3D]] = {}

for junction_box1 in junction_boxes:
  for junction_box2 in junction_boxes:
    if junction_box1 != junction_box2:
      d = point_distance(junction_box1, junction_box2)
      if d in distance_map:
        if junction_box1 not in distance_map[d]:
          raise ValueError
      else:
        distance_map[d] = (junction_box1, junction_box2)

distances = list(sorted(distance_map.keys()))
latest_join: tuple[Point3D, Point3D] | None = None
for distance in distances:
  if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
    break
  if distance not in distance_map:
    raise ValueError
  box1, box2 = distance_map[distance]
  circuit1: Circuit | None = circuit_pointers.get(box1)
  circuit2: Circuit | None = circuit_pointers.get(box2)
  if circuit1 and circuit2:
    if circuit1 is not circuit2:
      circuit1.update(circuit2)
      for box in circuit2:
        circuit_pointers[box] = circuit1
      circuits.remove(circuit2)
  elif not circuit1 and not circuit2:
    circuit = {box1, box2}
    circuits.append(circuit)
    circuit_pointers[box1] = circuit
    circuit_pointers[box2] = circuit
  elif circuit1 and not circuit2:
    circuit1.add(box2)
    circuit_pointers[box2] = circuit1
  elif circuit2 and not circuit1:
    circuit2.add(box1)
    circuit_pointers[box1] = circuit2
  latest_join = (box1, box2)

end_time = time.perf_counter() - start_time
if not latest_join:
  raise ValueError

box1, box2 = latest_join
print("Circuits value:", box1[0] * box2[0])
print(f"Time: {(end_time * 1000):.4f} ms")