def solve():
    t = int(input())
    out = []
    for _ in range(t):
        a, b = map(int, input().split())

        size = 1
        w1 = d1 = 0 
        w2 = d2 = 0 
        ans = 0

        layer = 1
        while True:
            if layer % 2 == 1:
                w1 += size
                d2 += size
            else:
                d1 += size
                w2 += size

            if (w1 <= a and d1 <= b) or (w2 <= a and d2 <= b):
                ans = layer
            else:
                break
            size *= 2
            layer += 1

        out.append(str(ans))

    print("\n".join(out))


solve()
