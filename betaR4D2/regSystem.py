def regUser():
    n = int(input())
    userReqs = {}
    response = []
    for i in range(n):
        reqs = input()
        if reqs not in userReqs:
            response.append("OK")
            userReqs[reqs] = 1
        else:
            response.append(reqs+str(userReqs[reqs]))
            userReqs[reqs] += 1
    for i in range(n):
        print(response[i])
regUser()