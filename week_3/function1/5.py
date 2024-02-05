import itertools

s =str(input())
str_perm = itertools.permutations(s)
str_perm = list(str_perm)
str_perm = [''.join(p) for p in str_perm]

print(str_perm)