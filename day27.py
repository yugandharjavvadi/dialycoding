'''Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''
#Answer



def isbalanced(s):
    l=[]
    for i in s:
        if i in'{([':
            l.append(i)
        elif i=='}':
            if len(l)==0 or l[-1]!='{':
                return False       
            else:
                l.pop()
        elif i==']':
            if len(l)==0 or l[-1]!='[':
                return False       
            else:
                l.pop()        
        elif i==')':
            if len(l)==0 or l[-1]!='(':
                return False       
            else:
                l.pop()   
        #print(l)                 
    return True            

s=input()
if isbalanced(s):
    print("Balanced")
else:
    print("Not Balanced")    
