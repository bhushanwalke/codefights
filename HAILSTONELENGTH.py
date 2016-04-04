__author__ = 'bhushan'

def hailstoneLength(l):
    if (l==1):
        return 2
    else:
        res = 4
        for i in range(2,l):
            r = int(res/3)
            if(r==1 or (r%2)==0):
                res = res*2
            else:
                res = int(res/3)
        return res


print(hailstoneLength(17))
