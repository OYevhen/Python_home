def rec(N, start=1):
    print(start)
    start += 1
    if start <= N:
        rec(N, start)


a = rec(5)
