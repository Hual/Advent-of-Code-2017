str = input()
count = 0

for i in range(len(str)):
  if str[i] == str[(i + (len(str) // 2)) % len(str)]:
    count += int(str[i])
    
print(count)
