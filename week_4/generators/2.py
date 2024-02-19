def funct(N):
    for i in range(N):
        if i%2==0:
            yield i
N=int(input())
for num in funct(N):
    print(num)