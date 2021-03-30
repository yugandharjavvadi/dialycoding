'''
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

'''

def dividearray(l, n):
	sum = 0
	i, j = 0, 0

	for i in range(n):
		sum += l[i]

	if sum % 2 != 0:
		return False

	part = [[True for i in range(n + 1)]
			for j in range(sum // 2 + 1)]

	for i in range(0, n + 1):
		part[0][i] = True

	for i in range(1, sum // 2 + 1):
		part[i][0] = False

	for i in range(1, sum // 2 + 1):

		for j in range(1, n + 1):
			part[i][j] = part[i][j - 1]

			if i >= l[j - 1]:
				part[i][j] = (part[i][j] or part[i - l[j - 1]][j - 1])

	return part[sum // 2][n]


l=[int(x) for x in input().split()]
n = len(l)

print(dividearray(l, n))
