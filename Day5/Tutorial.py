import math
li = [10,2,4,5,6]

max = -math.inf
for i in li:
   if i > max:
      max = i
print(max)

total = 0
for i in range(1, 101):
   total += i
print(total)