def spy_game(x):
    zeros=0
    sevens=False
    for i in x:
        if(i==0 and zeros==0):
            zeros+=1
        elif(i==0 and zeros==1):
            zeros+=1
        elif(i==7 and zeros==2):
            sevens=True
            break
    return sevens                    
print(spy_game([1,2,4,0,0,7,5]) )
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0])) 