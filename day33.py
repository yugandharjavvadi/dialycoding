'''Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:'''


l=[int(x) for x in input().split()]
n=len(l)
for i in range(1,n+1):
    r=l[:i]
    r.sort()
    if i%2:
        print(r[i//2])
    else:
        res=(r[i//2]+r[i//2-1])/2
        if res==int(res):
            res=int(res)
        print(res)    
