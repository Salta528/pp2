numheads=int(input())
numlegs=int(input())

def solve(heads,legs):
    rabbit_heads=int((legs-2*heads)/2)
    chicken_heads=int(heads-rabbit_heads)
    print(rabbit_heads,chicken_heads)

solve(numheads,numlegs)

     