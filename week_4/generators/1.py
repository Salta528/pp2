def funct(N):
    for i in range(N):
        if i**2<=N:
            yield i**2
N=int(input())
for num in funct(N):
    print(num)