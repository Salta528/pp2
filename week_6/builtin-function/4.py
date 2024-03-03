import time
def delayed_square_root(value, milliseconds):
    time.sleep(milliseconds / 1000) 
    result = value ** 0.5
    return result
x= int(input())
y= int(input())
result = delayed_square_root(x, y)
print("Square root of", x, "after", y, "milliseconds is ", result)