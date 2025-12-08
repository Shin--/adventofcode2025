import math
import time
from typing import Literal, NotRequired, TypeGuard, TypedDict, get_args


AllowedOperations = Literal['*', '+', '-', '%']

class Calculation(TypedDict):
  values: list[int]
  operation: NotRequired[AllowedOperations]

def is_allowed_operation(val: str) -> TypeGuard[AllowedOperations]:
    return val in get_args(AllowedOperations)

start_time = time.perf_counter()
calculations: list[Calculation] = list()
with open('python/day6/real_data.txt', 'r') as f:
  rows = f.readlines()
  for i, row in enumerate(rows):
    cols = row.split()
    if i == 0:
      calculations = [{'values': [int(col)]} for col in cols]
      continue

    for j, col in enumerate(cols):
      calculation = calculations[j]
      if i == (len(rows) - 1):
        if is_allowed_operation(col):
          calculation['operation'] = col
        else:
          raise ValueError
      else:
        calculation['values'].append(int(col))

calculations_sum = 0
for calculation in calculations:
  operation = calculation.get('operation')
  if not operation:
    print("Not good")
    break
  if operation == '*':
    calculations_sum += math.prod(calculation['values'])
  elif operation == '+':
    calculations_sum += sum(calculation['values'])

end_time = time.perf_counter() - start_time
print("Calculations sum:", calculations_sum)
print(f"Time: {(end_time * 1000):.4f} ms")