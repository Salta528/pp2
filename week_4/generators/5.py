def funct(a):
    for i in range(0,a+1):
            if i>0:
                a-=1
            yield a
a=int(input())
for num in funct(a):
    print(num)