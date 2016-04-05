'''
Let s(n, k) = sum[r * (r + 1) * (r + 2) * ... * (r + n)] where r runs from 1 to k.
Given n and k, your task is to find s(n,k).
'''

'''
Example
For n = 4 and k = 3, the output should be
SumItUp(n, k) = 3360.
s(4, 3) = 1 * 2 * 3 * 4 * 5 + 2 * 3 * 4 * 5 * 6 + 3 * 4 * 5 * 6 * 7.
'''


def SumItUp(n, k):
    sum = 0
    for r in range(1, k+1):
        res = r
        for j in range(1, n+1):
            f = r+j
            res = res * f
        sum += res
    return sum

print(SumItUp(4,3))
print(SumItUp(6, 7))