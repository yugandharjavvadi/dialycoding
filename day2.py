"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]"""
#solution

def remproduct(li):
    res=[]
    p=1
    zc=0
    for i in li:
        if i==0 and zc==0:
            zc+=1
            continue
        else:
            p*=i
    for i in li:
        if i==0:
            res.append(p)
        else:
            res.append(p//i)
    return res

li=[int(x) for x in input().split()]
print(remproduct(li))
