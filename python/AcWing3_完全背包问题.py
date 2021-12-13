N, V = map(int, input().split())
w = [0]
v = [0]
for i in range(N):
    a, b = input().split()
    v.append(int(a))
    w.append(int(b))

dp = [0 for _ in range(V+1)]

for i in range(1, N+1):
    for j in range(V+1):
        if j >= v[i]:
            dp[j] = max(dp[j], dp[j-v[i]]+w[i])

print(dp[V])