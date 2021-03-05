'''Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].'''
#Solution
def sortarr(l):
    rc=0
    gc=0
    bc=0
    for i in l:
        if i=='R':
            rc+=1
        elif i=='G':
            gc+=1
        else:
            bc+=1
    res=[]
    res.extend(['R']*rc)
    res.extend(['G']*gc)
    res.extend(['B']*bc)
    return res                



l=[x for x in input().split()]
res=sortarr(l)
print(res)