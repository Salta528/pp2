def histogram(number):
    for num in number:
        print('*' * num)
numbers=[]
x=int(input())
for i in range(x):
    numbers.append(int(input()))
histogram(numbers)


