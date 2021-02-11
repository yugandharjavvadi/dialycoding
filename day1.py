"""Given a list of numbers and a number k, return whether 
any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.
"""
#solution

def adduptok(lis,k):
    n=len(lis)
    lis.sort()
    l=0
    r=n-1
    while(l<r):
        s=lis[l]+lis[r]
        if s==k:
            return True
        elif s<k:
            l+=1
        else:
            r-=1
    return 0        

lis=[int(x) for x in input().split()]
k=int(input())
print(adduptok(lis,k))

        
