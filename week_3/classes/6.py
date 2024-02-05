def prime(number):
    if number<2:
        return False
    for i in range(2, int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True
numbers = []
x=int(input())
for i in range (x):
    numbers.append(int(input()))
prime_numbers = list(filter(lambda x: prime(x), numbers))
print(prime_numbers)