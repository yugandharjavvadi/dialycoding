'''Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.'''

def pow(x,y):
	if y == 0:
		return 1
	if y == 1:
		return x
	if y == -1:
		return 1/x
	if y % 2 == 0:
		return pow(x,y/2) * pow(x,y/2)
	else:
		return x * pow(x,(y-1)/2) * pow(x,(y-1)/2)


print(pow(2,10))
print(pow(3,5))
