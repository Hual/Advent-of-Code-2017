import sys

sum = 0

for line in sys.stdin:
  line = line.strip()
  if not line:
    break
  
  row = list(map(int, line.split('\t')))
  sum += max(row) - min(row)

print(sum)
