'''Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''
#solution

def classroomreq(l):
    finishtimes=[]
    for i in l:
        finishtimes.append(i[1])
    n=max(finishtimes)
    d=[0]*(n+1)
    for i in l:
        for j in range(i[0],i[1]+1):
            d[j]+=1
    return max(d) 
l=[(30, 75), (0, 50), (60, 150)]   
print(classroomreq(l))
 