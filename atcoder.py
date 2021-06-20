#206 B

import sys

n = int(input())
count = 0
x = 0

while True:
    count += 1
    x += count

    if n <= x:
        print(count)
        sys.exit()