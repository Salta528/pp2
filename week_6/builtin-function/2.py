def funct(string):
    upper_cnt = 0
    lower_cnt = 0
    for char in string:
        if char.isupper():
            upper_cnt = sum([1], start=upper_cnt)
        elif char.islower():   
            lower_cnt = sum([1], start=lower_cnt)
    return upper_cnt, lower_cnt
s=str(input())
upper, lower = funct(s)

print("uppercase letters:", upper)
print("lowercase letters:",lower)