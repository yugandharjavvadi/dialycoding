'''Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether 
the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', 
you should return true, since it's the last row.
'''

def find_string(m,s):
    for i in m:
        s1=''.join(i)
        if s in s1:
            return True
    m1=[[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]    
    print(m1)
            
    
    for i in m1:
        s1=''.join(i)
        if s in s1:
            return True        
    return False


m=[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']] 
print(find_string(m,"FOAM"))
print(find_string(m,"MASS") )

