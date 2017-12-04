import sys
import itertools

count = 0

for line in sys.stdin:
  line = line.strip()
  if not line:
    break
  
  for a, b in itertools.combinations(line.split(' '), 2):
    if sorted(a) == sorted(b):
      break
  else:
    count += 1

print(count)
