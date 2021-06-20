#206 C

from collections import Counter

n = int(input())
N = [int(i) for i in range(n)]
A = list(map(int, input().split()))
A_ = Counter(A)
ans = 0
total = 0

for i in range(len(A) - 1, 0, -1):
    ans += i

for j in A_:
    count = 0
    if A_[j] != 1:
        for k in range(1, A_[j]):
            count += k
        ans = ans - count

print(ans)