import sys
import itertools

count = 0

for line in sys.stdin:
  line = line.strip()
  if not line:
    break
  
  words = line.split(' ')
  if len(set(words)) == len(words):
    count += 1

print(count)
