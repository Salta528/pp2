def palindrome(a):
    p=a[::-1]
    if a==p:
        return True
    else:
        return False
s=str(input())
print(palindrome(s))
