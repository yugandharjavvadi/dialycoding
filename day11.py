'''Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
'''

def prematch(querystringset,prefix):
    res=[]
    for i in querystringset:
        if i.startswith(prefix):
            res.append(i)
    return res        
querystringset=[x for x in input().split()]
prefix=input()
print(prematch(querystringset,prefix))