
def solve():
    d, total = map(int, input().split())
    minTime = []
    maxTime = []
    for i in range(d):
        m, M = map(int, input().split())
        minTime.append(m)
        maxTime.append(M)

    minSum = sum(minTime)
    maxSum = sum(maxTime)

    if total < minSum or total > maxSum:
        print("NO")
        return

    schedule = minTime[:]

    rem = total - minSum

    for i in range(d):
        add = min(rem, maxTime[i] - schedule[i])
        schedule[i]+=add
        rem-=add

        if rem == 0:
            break

    print("YES")
    print(*schedule)

solve()




