'''Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''
#Answer
def encode(s):
    res=""
    p=s[0]
    c=0
    for i in s:
        if i==p:
            c+=1
        else:
            res+=str(c)
            res+=p
            p=i
            c=1
    res+=str(c)
    res+=p        
    return res


def decode(s):
    d=''
    res=''
    for i in s:
        if i.isdigit():
            d+=i
        else:
            res+=int(d)*i
            d=''
    return res 

s="AAAABBBBABBABA"
encoded_string=encode(s)
print(encoded_string)
decode_string=decode(encoded_string)
print(decode_string)



