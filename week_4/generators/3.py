def funct(N):
    for i in range(N):
        if i%3==0 and i%4==0:
            yield i
N=int(input())
for num in funct(N):
    print(num)