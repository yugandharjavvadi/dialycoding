'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
'''

#solution
def no_of_ways(n):
    l=[1,2]
    for i in range(n-2):
        l.append(l[-1]+l[-2])
    return l[n-1]    

n=int(input())
print(no_of_ways(n))
