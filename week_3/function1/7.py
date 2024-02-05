def has_33(a):
    for i in range(1,len(a)-1):
        if a[i] == 3 and a[i+1] == 3:
            return True
        else:
            return False
a = []
x=int(input())
for i in range(x):
    a.append(int(input()))
print(has_33(a))


"""
def has_33(a):
    for i in range(len(a)):
        if(a[i]==3 and a[i+1]==3):
            return true
        elif(a[i]==3 and a[i+1]!=3):
            return false
        elif(a[i]!=3 and a[i+1]==3):
            return false

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
"""