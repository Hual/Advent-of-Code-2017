import sys
import itertools

sum = 0

for line in sys.stdin:
  line = line.strip()
  if not line:
    break
  
  row = list(map(int, line.split('\t')))
  for a, b in itertools.combinations(row, 2):
    if max(a, b) % min(a, b) == 0:
      sum += max(a, b) // min(a, b)
      break

print(sum)
