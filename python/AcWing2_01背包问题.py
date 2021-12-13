N, V = map(int, input().split())
w = [0]
v = [0]
for i in range(N):
    a, b = input().split()
    v.append(int(a))
    w.append(int(b))

dp = [[0 for _ in range(V+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1,V+1):
        dp[i][j] = dp[i-1][j]
        if j >= v[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]]+w[i])

print(dp[N][V])