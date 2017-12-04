str = input()
count = 0

for i in range(len(str)):
  if str[i] == str[(i + 1) % len(str)]:
    count += int(str[i])
    
print(count)
