from bisect import bisect_left
def formEnvChain():
    n, w, h = map(int, input().split())
    env = []
    for idx in range(1, n + 1):
        wi, hi = map(int, input().split())
        if wi > w and hi > h:
            env.append((wi, hi, idx))

    if not env:
        print(0)
        return

    env.sort(key=lambda x: (x[0], -x[1]))

    m = len(env)
    tails_height = []
    tails_pos = []

    parent = [-1] * m 

    for i in range(m):
        hi = env[i][1]

        pos = bisect_left(tails_height, hi)

        if pos == len(tails_height):
            tails_height.append(hi)
            tails_pos.append(i)
        else:
            tails_height[pos] = hi
            tails_pos[pos] = i

        if pos > 0:
            parent[i] = tails_pos[pos - 1]

    length = len(tails_height)
    cur = tails_pos[-1]
    ans = []
    while cur != -1:
        ans.append(env[cur][2])
        cur = parent[cur]
    ans.reverse()

    print(length)
    print(*ans)
formEnvChain()
