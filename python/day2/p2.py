import re


repeating_patterns_sum = 0
with open('python/day2/data.txt', 'r') as f:
  for l in f.readlines():
    ranges = l.split(',')
    for r in ranges:
      start, end = r.split('-')
      for id in range(int(start), int(end)+1):
        invalid_ids: set[int] = set()
        id_str = str(id)
        id_length = len(id_str)
        for sequence_length in range(1, id_length//2+1):
          if id_length % sequence_length == 0:
            sequences = re.findall('.'*sequence_length, id_str)
            if len(set(sequences)) == 1:
              invalid_ids.add(id)
        repeating_patterns_sum += sum(invalid_ids)
print("Repeating patterns sum:", repeating_patterns_sum)