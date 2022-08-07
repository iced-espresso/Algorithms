import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
bag = [(0, 0)]
for _ in range(N):
    W, V = map(int, sys.stdin.readline().rstrip().split())
    bag.append((W, V))
    
dp = [[0]*(K+1) for _ in range(N+1)]

for y in range(1, N+1):
    w, v = bag[y]
    for x in range(1, K+1):
        if x-w <= 0:
            dp[y][x] = dp[y-1][x]
        else:
            dp[y][x] = max(dp[y-1][x], dp[y-1][x-w] + v)

print(dp[N][K])