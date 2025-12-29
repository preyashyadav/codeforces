def solve():

    t = int(input())
    response = []
    for i in range(t):
        l = int(input())
        s = str(input())
        if "2026" in s or "2025" not in s:
            response.append(0)
        elif "2025" in s:
            response.append(1)
            
    for i in range(len(response)):
        print(response[i])
solve()