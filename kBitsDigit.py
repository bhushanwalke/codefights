"""
Return a list of all numbers that have no more than n bits, such that exactly k of them are set to 1.

Example

For n = 4 and k = 1, the output should be
kBitsDigits(n, k) = [1,2,4,8].

110 = 12, which obviously has 1 < 4 number of bits, and the only bit is 1.
210 = 102, which has 2 < 4 number of bits, with the first one equal to 1.
410 = 1002, which has 3 < 4 number of bits, with the first one equal to 1.
810 = 102, which has 3 < 4 number of bits, with the first one equal to 1.
"""

def kBitsDigits(n, k):
    flag = True
    num = 1
    res = []
    if k == 0:
        return [0]
    else:
        while flag:
            bin_num = (bin(num)[2:])
            if len(bin_num) < n+1:
                k_count = 0
                for i in bin_num:
                    if i == '1':
                        k_count +=1
                if k_count == k:
                    res.append(num)
            else:
                flag = False
            num +=1
        return res

print kBitsDigits(5,5)
print kBitsDigits(3,20)
print kBitsDigits(4,1)

