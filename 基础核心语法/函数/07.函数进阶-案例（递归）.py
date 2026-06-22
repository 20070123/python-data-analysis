#案例一：输入一个数，算他的阶乘
def jc(n):
    if n==1:
        return n
    else:
        return n*jc(n-1)
s=jc(3)
print(s)

