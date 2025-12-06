repeating_patterns_sum = 0
with open('python/day2/data.txt', 'r') as f:
  for l in f.readlines():
    ranges = l.split(',')
    for r in ranges:
      start, end = r.split('-')
      for id in range(int(start), int(end)+1):
        id_str = str(id)
        id_length = len(id_str)
        if id_length % 2 == 0:
          if id_str[0:id_length//2] == id_str[id_length//2:]:
            repeating_patterns_sum += id
print("Repeating patterns sum:", repeating_patterns_sum)