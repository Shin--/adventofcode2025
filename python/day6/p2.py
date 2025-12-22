from dataclasses import dataclass
import math
import re
import time
from typing import Literal, NotRequired, TypeGuard, TypedDict, get_args


AllowedOperations = Literal['*', '+', '-', '%'] 

@dataclass
class Calculation:
  column_values: list[list[str]]
  column_pos: tuple[int, int]
  operation: AllowedOperations | None = None

  @property
  def right_to_left_columns(self) -> list[int]:
    return[int("".join(col_vals)) for col_vals in self.column_values]
  
  @property
  def result(self) -> int:
    if self.operation == '*':
      return math.prod(self.right_to_left_columns)
    elif self.operation == '+':
      return sum(self.right_to_left_columns)
    raise ValueError

def is_allowed_operation(val: str) -> TypeGuard[AllowedOperations]:
    return val in get_args(AllowedOperations)

start_time = time.perf_counter()
calculations: list[Calculation] = list()
with open('python/day6/data.txt', 'r') as f:
  rows = f.readlines()
  for i, row in enumerate(reversed(rows)):
    if i == 0:
      operator_indices = [x.start() for x in re.finditer(r'[\\+\\*]', row)]
      for j, operator_index in enumerate(operator_indices):
        if j < (len(operator_indices) - 1):
          col_end = operator_indices[j + 1] - 1
        else:
          col_end = len(row)
        operator = row[operator_index]
        if is_allowed_operation(operator):
          calculations.append(
            Calculation(
              column_values=[list() for x in range(col_end - operator_index)], 
              column_pos=(operator_index, col_end), 
              operation=operator
            )
          )
        else:
          raise ValueError
    else:
      for calculation in calculations:
        row_start, row_end = calculation.column_pos
        for col_i, col_val in enumerate(reversed(row[row_start:row_end])):
          calculation.column_values[col_i].insert(0, col_val)

calculations_sum = 0
for calculation in calculations:
  calculations_sum += calculation.result

end_time = time.perf_counter() - start_time
print("Calculations sum:", calculations_sum)
print(f"Time: {(end_time * 1000):.4f} ms")